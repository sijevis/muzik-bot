import sqlite3
import os
import json
import logging
from datetime import datetime
from firebase_config import is_firebase_available, get_firestore_client

logger = logging.getLogger(__name__)

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "muzikbot.db")


class MemoryStore:
    def __init__(self, db_path=None):
        self.db_path = db_path or DB_PATH
        self.use_firebase = is_firebase_available()
        self._init_db()
        if self.use_firebase:
            logger.info("Firebase Firestore modu aktif")
        else:
            logger.info("SQLite modu aktif")

    def _init_db(self):
        if self.use_firebase:
            firestore = get_firestore_client()
            try:
                firestore.collection("users").limit(1).get()
                logger.info("Firestore koleksiyonlari hazir")
            except Exception as e:
                logger.warning(f"Firestore kontrol hatasi: {e}")
            return

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                display_name TEXT DEFAULT 'Kullanici',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS preferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                category TEXT NOT NULL,
                value TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                UNIQUE(user_id, category, value)
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                analysis TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS playlists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_id TEXT,
                name TEXT,
                description TEXT,
                preferences TEXT,
                song_count INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS playlist_songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                playlist_id INTEGER NOT NULL,
                song_name TEXT NOT NULL,
                artist TEXT NOT NULL,
                album TEXT,
                genre TEXT,
                mood TEXT,
                language TEXT,
                cover_url TEXT,
                spotify_url TEXT,
                reason TEXT,
                position INTEGER DEFAULT 0,
                FOREIGN KEY (playlist_id) REFERENCES playlists(id)
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                email TEXT UNIQUE,
                password_hash TEXT,
                display_name TEXT DEFAULT 'Kullanici',
                spotify_connected INTEGER DEFAULT 0,
                spotify_access_token TEXT,
                spotify_refresh_token TEXT,
                spotify_token_expires REAL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def ensure_user(self, user_id, display_name=None):
        if self.use_firebase:
            firestore = get_firestore_client()
            user_ref = firestore.collection("users").document(user_id)
            doc = user_ref.get()
            if not doc.exists:
                user_ref.set({
                    "display_name": display_name or "Kullanici",
                    "created_at": datetime.utcnow().isoformat(),
                })
            elif display_name:
                user_ref.update({"display_name": display_name})

        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        if not c.fetchone():
            c.execute(
                "INSERT INTO users (user_id, display_name) VALUES (?, ?)",
                (user_id, display_name or "Kullanici"),
            )
            conn.commit()
        elif display_name:
            c.execute(
                "UPDATE users SET display_name = ? WHERE user_id = ?",
                (display_name, user_id),
            )
            conn.commit()
        conn.close()

    def add_preference(self, user_id, category, value):
        self.ensure_user(user_id)

        if self.use_firebase:
            firestore = get_firestore_client()
            pref_id = f"{category}_{value}"
            firestore.collection("users").document(user_id).collection("preferences").document(pref_id).set({
                "category": category,
                "value": value,
                "created_at": datetime.utcnow().isoformat(),
            })

        conn = self._get_conn()
        try:
            conn.execute(
                "INSERT OR IGNORE INTO preferences (user_id, category, value) VALUES (?, ?, ?)",
                (user_id, category, value),
            )
            conn.commit()
        except sqlite3.IntegrityError:
            pass
        finally:
            conn.close()

    def remove_preference(self, user_id, category, value):
        if self.use_firebase:
            firestore = get_firestore_client()
            pref_id = f"{category}_{value}"
            firestore.collection("users").document(user_id).collection("preferences").document(pref_id).delete()

        conn = self._get_conn()
        conn.execute(
            "DELETE FROM preferences WHERE user_id = ? AND category = ? AND value = ?",
            (user_id, category, value),
        )
        conn.commit()
        conn.close()

    def get_preferences(self, user_id):
        self.ensure_user(user_id)

        if self.use_firebase:
            firestore = get_firestore_client()
            prefs_docs = firestore.collection("users").document(user_id).collection("preferences").get()
            prefs = {
                "liked_genres": [],
                "disliked_genres": [],
                "liked_artists": [],
                "disliked_artists": [],
                "liked_moods": [],
                "preferred_language": None,
            }
            for doc in prefs_docs:
                data = doc.to_dict()
                cat = data.get("category", "")
                val = data.get("value", "")
                if cat == "liked_genre":
                    prefs["liked_genres"].append(val)
                elif cat == "disliked_genre":
                    prefs["disliked_genres"].append(val)
                elif cat == "liked_artist":
                    prefs["liked_artists"].append(val)
                elif cat == "disliked_artist":
                    prefs["disliked_artists"].append(val)
                elif cat == "liked_mood":
                    prefs["liked_moods"].append(val)
                elif cat == "preferred_language":
                    prefs["preferred_language"] = val
            return prefs

        conn = self._get_conn()
        c = conn.cursor()
        c.execute(
            "SELECT category, value FROM preferences WHERE user_id = ?", (user_id,)
        )
        rows = c.fetchall()
        conn.close()
        prefs = {
            "liked_genres": [],
            "disliked_genres": [],
            "liked_artists": [],
            "disliked_artists": [],
            "liked_moods": [],
            "preferred_language": None,
        }
        for cat, val in rows:
            if cat == "liked_genre":
                prefs["liked_genres"].append(val)
            elif cat == "disliked_genre":
                prefs["disliked_genres"].append(val)
            elif cat == "liked_artist":
                prefs["liked_artists"].append(val)
            elif cat == "disliked_artist":
                prefs["disliked_artists"].append(val)
            elif cat == "liked_mood":
                prefs["liked_moods"].append(val)
            elif cat == "preferred_language":
                prefs["preferred_language"] = val
        return prefs

    def get_memory_summary(self, user_id):
        self.ensure_user(user_id)
        prefs = self.get_preferences(user_id)

        recent = self.get_conversation(user_id, limit=6)

        summary_parts = []
        if prefs["liked_genres"]:
            summary_parts.append(f"Sevdigi turler: {', '.join(prefs['liked_genres'])}")
        if prefs["disliked_genres"]:
            summary_parts.append(f"Sevmedigi turler: {', '.join(prefs['disliked_genres'])}")
        if prefs["liked_artists"]:
            summary_parts.append(f"Sevdigi sanatcilar: {', '.join(prefs['liked_artists'])}")
        if prefs["preferred_language"]:
            summary_parts.append(f"Dil tercihi: {prefs['preferred_language']}")
        recent_msgs = [f"{m['role']}: {m['content']}" for m in recent[:6]]
        if recent_msgs:
            summary_parts.append(f"Son konusmalar: {'; '.join(recent_msgs)}")
        return " | ".join(summary_parts) if summary_parts else ""

    def save_message(self, user_id, session_id, role, content, analysis=None):
        self.ensure_user(user_id)

        if self.use_firebase:
            firestore = get_firestore_client()
            firestore.collection("conversations").add({
                "user_id": user_id,
                "session_id": session_id,
                "role": role,
                "content": content,
                "analysis": json.dumps(analysis) if analysis else None,
                "created_at": datetime.utcnow().isoformat(),
            })

        conn = self._get_conn()
        conn.execute(
            "INSERT INTO conversations (user_id, session_id, role, content, analysis) VALUES (?, ?, ?, ?, ?)",
            (user_id, session_id, role, content, json.dumps(analysis) if analysis else None),
        )
        conn.commit()
        conn.close()

    def get_conversation(self, user_id, session_id=None, limit=20):
        self.ensure_user(user_id)

        if self.use_firebase:
            firestore = get_firestore_client()
            query = firestore.collection("conversations").where("user_id", "==", user_id).order_by("created_at", direction="DESCENDING").limit(limit)
            if session_id:
                query = query.where("session_id", "==", session_id)
            docs = query.get()
            messages = [{"role": doc.to_dict().get("role", ""), "content": doc.to_dict().get("content", "")} for doc in docs]
            return list(reversed(messages))

        conn = self._get_conn()
        c = conn.cursor()
        if session_id:
            c.execute(
                "SELECT role, content FROM conversations WHERE user_id = ? AND session_id = ? ORDER BY created_at DESC LIMIT ?",
                (user_id, session_id, limit),
            )
        else:
            c.execute(
                "SELECT role, content FROM conversations WHERE user_id = ? ORDER BY created_at DESC LIMIT ?",
                (user_id, limit),
            )
        rows = c.fetchall()
        conn.close()
        return [{"role": r, "content": c} for r, c in reversed(rows)]

    def clear_conversation(self, user_id, session_id):
        if self.use_firebase:
            firestore = get_firestore_client()
            docs = firestore.collection("conversations").where("user_id", "==", user_id).where("session_id", "==", session_id).get()
            for doc in docs:
                doc.reference.delete()

        conn = self._get_conn()
        conn.execute(
            "DELETE FROM conversations WHERE user_id = ? AND session_id = ?",
            (user_id, session_id),
        )
        conn.commit()
        conn.close()

    def save_playlist(self, user_id, session_id, name, description, preferences, songs):
        self.ensure_user(user_id)

        if self.use_firebase:
            firestore = get_firestore_client()
            playlist_ref = firestore.collection("playlists").document()
            playlist_ref.set({
                "user_id": user_id,
                "session_id": session_id,
                "name": name,
                "description": description,
                "preferences": preferences,
                "song_count": len(songs),
                "created_at": datetime.utcnow().isoformat(),
            })
            for i, song in enumerate(songs):
                playlist_ref.collection("songs").document(str(i)).set({
                    "position": i,
                    "name": song.get("name", ""),
                    "artist": song.get("artist", ""),
                    "album": song.get("album", ""),
                    "genre": song.get("genre", ""),
                    "mood": song.get("mood", ""),
                    "language": song.get("language", ""),
                    "cover_url": song.get("cover_url", ""),
                    "spotify_url": song.get("spotify_url", ""),
                    "reason": song.get("reason", ""),
                })

        conn = self._get_conn()
        c = conn.cursor()
        c.execute(
            "INSERT INTO playlists (user_id, session_id, name, description, preferences, song_count) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, session_id, name, description, json.dumps(preferences), len(songs)),
        )
        playlist_id = c.lastrowid
        for i, song in enumerate(songs):
            c.execute(
                "INSERT INTO playlist_songs (playlist_id, song_name, artist, album, genre, mood, language, cover_url, spotify_url, reason, position) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    playlist_id,
                    song.get("name", ""),
                    song.get("artist", ""),
                    song.get("album", ""),
                    song.get("genre", ""),
                    song.get("mood", ""),
                    song.get("language", ""),
                    song.get("cover_url", ""),
                    song.get("spotify_url", ""),
                    song.get("reason", ""),
                    i,
                ),
            )
        conn.commit()
        conn.close()
        return playlist_id

    def get_playlists(self, user_id, limit=10):
        self.ensure_user(user_id)

        if self.use_firebase:
            firestore = get_firestore_client()
            docs = firestore.collection("playlists").where("user_id", "==", user_id).order_by("created_at", direction="DESCENDING").limit(limit).get()
            playlists = []
            for doc in docs:
                data = doc.to_dict()
                playlists.append({
                    "id": doc.id,
                    "name": data.get("name", ""),
                    "description": data.get("description", ""),
                    "preferences": data.get("preferences", {}),
                    "song_count": data.get("song_count", 0),
                    "created_at": data.get("created_at", ""),
                })
            return playlists

        conn = self._get_conn()
        c = conn.cursor()
        c.execute(
            "SELECT id, name, description, preferences, song_count, created_at FROM playlists WHERE user_id = ? ORDER BY created_at DESC LIMIT ?",
            (user_id, limit),
        )
        playlists = []
        for row in c.fetchall():
            pid, name, desc, prefs_json, count, created = row
            playlists.append({
                "id": pid,
                "name": name,
                "description": desc,
                "preferences": json.loads(prefs_json) if prefs_json else {},
                "song_count": count,
                "created_at": created,
            })
        conn.close()
        return playlists

    def get_playlist_songs(self, playlist_id):
        if self.use_firebase and isinstance(playlist_id, str):
            firestore = get_firestore_client()
            songs_docs = firestore.collection("playlists").document(playlist_id).collection("songs").order_by("position").get()
            return [
                {
                    "name": doc.to_dict().get("name", ""),
                    "artist": doc.to_dict().get("artist", ""),
                    "album": doc.to_dict().get("album", ""),
                    "genre": doc.to_dict().get("genre", ""),
                    "mood": doc.to_dict().get("mood", ""),
                    "language": doc.to_dict().get("language", ""),
                    "cover_url": doc.to_dict().get("cover_url", ""),
                    "spotify_url": doc.to_dict().get("spotify_url", ""),
                    "reason": doc.to_dict().get("reason", ""),
                }
                for doc in songs_docs
            ]

        conn = self._get_conn()
        c = conn.cursor()
        c.execute(
            "SELECT song_name, artist, album, genre, mood, language, cover_url, spotify_url, reason FROM playlist_songs WHERE playlist_id = ? ORDER BY position",
            (playlist_id,),
        )
        rows = c.fetchall()
        conn.close()
        return [
            {
                "name": r[0],
                "artist": r[1],
                "album": r[2],
                "genre": r[3],
                "mood": r[4],
                "language": r[5],
                "cover_url": r[6],
                "spotify_url": r[7],
                "reason": r[8],
            }
            for r in rows
        ]

    def update_preferences_from_analysis(self, user_id, analysis):
        if analysis.get("genre"):
            self.add_preference(user_id, "liked_genre", analysis["genre"])
        if analysis.get("mood"):
            self.add_preference(user_id, "liked_mood", analysis["mood"])
        if analysis.get("artist"):
            self.add_preference(user_id, "liked_artist", analysis["artist"])
        if analysis.get("language"):
            self.add_preference(user_id, "preferred_language", analysis["language"])

    def get_context_for_llm(self, user_id, limit=10):
        history = self.get_conversation(user_id, limit=limit)
        prefs = self.get_preferences(user_id)
        summary = self.get_memory_summary(user_id)
        return {"history": history, "preferences": prefs, "summary": summary}

    def register_user(self, email, password_hash, display_name=None):
        conn = self._get_conn()
        c = conn.cursor()
        try:
            user_id = email
            c.execute(
                "INSERT INTO accounts (user_id, email, password_hash, display_name) VALUES (?, ?, ?, ?)",
                (user_id, email, password_hash, display_name or "Kullanici"),
            )
            conn.commit()
            self.ensure_user(user_id, display_name)
            return {"user_id": user_id, "email": email, "display_name": display_name or "Kullanici"}
        except sqlite3.IntegrityError:
            conn.close()
            return None
        finally:
            conn.close()

    def login_user(self, email, password_hash):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT user_id, email, display_name, spotify_connected FROM accounts WHERE email = ? AND password_hash = ?", (email, password_hash))
        row = c.fetchone()
        conn.close()
        if row:
            return {"user_id": row[0], "email": row[1], "display_name": row[2], "spotify_connected": bool(row[3])}
        return None

    def get_user(self, user_id):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT user_id, email, display_name, spotify_connected FROM accounts WHERE user_id = ?", (user_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return {"user_id": row[0], "email": row[1], "display_name": row[2], "spotify_connected": bool(row[3])}
        return None

    def get_user_by_email(self, email):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT user_id, email, display_name, password_hash, spotify_connected FROM accounts WHERE email = ?", (email,))
        row = c.fetchone()
        conn.close()
        if row:
            return {"user_id": row[0], "email": row[1], "display_name": row[2], "password_hash": row[3], "spotify_connected": bool(row[4])}
        return None

    def link_spotify(self, user_id, access_token, refresh_token, expires_at):
        conn = self._get_conn()
        conn.execute(
            "UPDATE accounts SET spotify_connected = 1, spotify_access_token = ?, spotify_refresh_token = ?, spotify_token_expires = ? WHERE user_id = ?",
            (access_token, refresh_token, expires_at, user_id),
        )
        conn.commit()
        conn.close()

        if self.use_firebase:
            try:
                firestore = get_firestore_client()
                firestore.collection("users").document(user_id).update({
                    "spotify_connected": True,
                    "spotify_access_token": access_token,
                    "spotify_refresh_token": refresh_token,
                    "spotify_token_expires": expires_at,
                })
            except Exception:
                pass

    def unlink_spotify(self, user_id):
        conn = self._get_conn()
        conn.execute(
            "UPDATE accounts SET spotify_connected = 0, spotify_access_token = NULL, spotify_refresh_token = NULL, spotify_token_expires = 0 WHERE user_id = ?",
            (user_id,),
        )
        conn.commit()
        conn.close()

    def get_spotify_tokens(self, user_id):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT spotify_access_token, spotify_refresh_token, spotify_token_expires FROM accounts WHERE user_id = ?", (user_id,))
        row = c.fetchone()
        conn.close()
        if row and row[0]:
            return {"access_token": row[0], "refresh_token": row[1], "expires_at": row[2]}
        return None

    def rename_playlist(self, playlist_id, name):
        conn = self._get_conn()
        conn.execute("UPDATE playlists SET name = ? WHERE id = ?", (name, playlist_id))
        conn.commit()
        conn.close()

    def get_playlist_by_id(self, playlist_id):
        conn = self._get_conn()
        c = conn.cursor()
        c.execute("SELECT id, user_id, name, description, preferences, song_count, created_at FROM playlists WHERE id = ?", (playlist_id,))
        row = c.fetchone()
        conn.close()
        if not row:
            return None
        return {
            "id": row[0],
            "user_id": row[1],
            "name": row[2],
            "description": row[3],
            "preferences": json.loads(row[4]) if row[4] else {},
            "song_count": row[5],
            "created_at": row[6],
        }

    def delete_playlist(self, playlist_id, user_id=None):
        conn = self._get_conn()
        conn.execute("DELETE FROM playlist_songs WHERE playlist_id = ?", (playlist_id,))
        if user_id:
            conn.execute("DELETE FROM playlists WHERE id = ? AND user_id = ?", (playlist_id, user_id))
        else:
            conn.execute("DELETE FROM playlists WHERE id = ?", (playlist_id,))
        conn.commit()
        conn.close()