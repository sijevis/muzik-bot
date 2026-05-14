from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import sys
import io
import random
import hashlib
import json
import logging
import secrets
from dotenv import load_dotenv
from urllib.parse import quote

logger = logging.getLogger(__name__)

load_dotenv()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from memory import MemoryStore
from analyzer import MessageAnalyzer, ResponseGenerator, CATEGORY_LIST
from music_service import MusicClient
from llm_service import LLMClient
from playlist import PlaylistGenerator, PlaylistQuestioner
from demo_data import DEMO_SONGS
from firebase_config import is_firebase_available, verify_firebase_token

app = Flask(__name__)
CORS(app, origins="*", allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST", "OPTIONS"])

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

memory = MemoryStore()
analyzer = MessageAnalyzer()
response_generator = ResponseGenerator()
music_client = MusicClient()
llm_client = LLMClient()
playlist_generator = PlaylistGenerator()
playlist_questioner = PlaylistQuestioner()

DEMO_MODE = music_client.demo_mode and llm_client.demo_mode

playlist_sessions = {}
conversation_states = {}

PLAYLIST_NAME_SUGGESTIONS = {
    "rock": ["Rock Zamanı", "Gitar Fırtınası", "Rock Rüzgarı"],
    "pop": ["Pop Dalgası", "Neşeli Ritimler", "Pop Sahne"],
    "rap": ["Rap Akışı", "Beat Dalgası", "Mikrofon Sesi"],
    "jazz": ["Caz Gecesi", "Sakin Caz", "Jazz&Rüzgar"],
    "klasik": ["Klasik Anlar", "Piyano Nağmeleri", "Senfonik Yolculuk"],
    "elektronik": ["Elektronik Gece", "Bass Titreşimi", "Synth Yıldızları"],
    "rnb": ["R&B Akşamı", "Soul Dokunuşu", "Ritim ve Blues"],
    "turkce_rock": ["Türkçe Rock", "Anadolu Rüzgarı", "Gitar veTürkçe"],
    "turkce_pop": ["Türkçe Pop", "PopTürk", "Eğlence Zamanı"],
    "lofi": ["Lo-Fi Odak", "Sakinleştirici Lo-Fi", "Çalışma Ritmi"],
    "metal": ["Metal Fırtınası", "Ağır Ritimler", "Metal Gücü"],
    "arabesk": ["Arabesk Gecesi", "Duygusal Şarkılar", "Gönül Ezgileri"],
    "indie": ["Indie Keşif", "Alternatif Dünya", "Bağımsız Ritim"],
    "blues": ["Blues Gecesi", "Mavi Nağmeler", "Blues ve Rüzgar"],
    "default": ["Karma Playlist", "Müzik Zamanı", "Keşfet"],
}


def suggest_playlist_name(preferences):
    genres = preferences.get("genres", [])
    mood = preferences.get("mood")
    mood_names = {"uzgun": "Hüzünlü", "mutlu": "Neşeli", "enerjik": "Enerjik", "sakin": "Sakin", "romantik": "Romantik", "motivasyon": "Motivasyon"}
    if genres:
        genre = genres[0]
        names = PLAYLIST_NAME_SUGGESTIONS.get(genre, PLAYLIST_NAME_SUGGESTIONS["default"])
        name = random.choice(names)
    elif mood:
        prefix = mood_names.get(mood, "")
        name = f"{prefix} Müzik Zamanı" if prefix else random.choice(PLAYLIST_NAME_SUGGESTIONS["default"])
    else:
        name = random.choice(PLAYLIST_NAME_SUGGESTIONS["default"])
    return name


def _hash_password(password):
    salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return f"{salt}:{key.hex()}"

def _verify_password(password, stored_hash):
    try:
        salt, key_hex = stored_hash.split(':', 1)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
        return key.hex() == key_hex
    except (ValueError, AttributeError):
        return hashlib.sha256(password.encode()).hexdigest() == stored_hash


@app.route("/api/chat", methods=["POST"])
@limiter.limit("30/minute")
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({
                "error": "Mesaj alanı zorunludur.",
                "message": "Bir mesaj göndermen gerekiyor! Ne tür müzik istersin?",
                "songs": [],
                "ask_more": True,
                "playlist": None,
                "playlist_question": None,
            }), 400

        user_message = data["message"].strip()
        session_id = data.get("session_id", "default")
        user_id = data.get("user_id", session_id)

        if not user_message:
            return jsonify({
                "error": "Mesaj boş olamaz.",
                "message": "Bir şey yaz bakalım!",
                "songs": [],
                "ask_more": True,
                "playlist": None,
                "playlist_question": None,
            }), 400

        memory.ensure_user(user_id)
        memory.save_message(user_id, session_id, "user", user_message)

        user_prefs = memory.get_preferences(user_id)
        analysis = analyzer.analyze(user_message)
        analysis["user_id"] = user_id

        memory.update_preferences_from_analysis(user_id, analysis)

        is_playlist = playlist_generator.is_playlist_request(user_message)

        if analysis.get("artist") and not any(k.startswith("tur:") for k in analysis.get("keywords", [])):
            if "liste" not in user_message.lower() and "playlist" not in user_message.lower():
                is_playlist = False

        if not is_playlist and session_id in playlist_sessions:
            prefs = playlist_sessions[session_id]
            next_question = playlist_questioner.get_next_question(prefs)
            if next_question:
                answer = playlist_questioner.parse_answer(next_question["key"], user_message)
                if answer is not None:
                    prefs[next_question["key"]] = answer
                    playlist_sessions[session_id] = prefs

                    next_q = playlist_questioner.get_next_question(prefs)
                    if next_q:
                        question_msg = next_q["question"] + "\n\n"
                        for i, opt in enumerate(next_q["options"]):
                            question_msg += f"{i+1}. {opt}\n"

                        memory.save_message(user_id, session_id, "assistant", question_msg)
                        return jsonify({
                            "message": question_msg,
                            "songs": [],
                            "ask_more": False,
                            "analysis": analysis,
                            "demo_mode": DEMO_MODE,
                            "playlist": None,
                            "playlist_question": {"key": next_q["key"], "question": next_q["question"], "options": next_q["options"]},
                        })
                    else:
                        is_playlist = True

        if is_playlist:
            prefs = playlist_generator.detect_preferences(user_message, analysis)
            if session_id in playlist_sessions:
                stored = playlist_sessions[session_id]
                for key, val in stored.items():
                    if val is not None and prefs.get(key) is None:
                        prefs[key] = val

            playlist_sessions[session_id] = prefs
            has_prefs = (
                len(prefs.get("genres", [])) > 0
                or prefs.get("mood")
                or prefs.get("activity")
                or prefs.get("language")
            )

            if has_prefs or prefs.get("energy") or prefs.get("count", 10) != 10:
                playlist_result = playlist_generator.generate_playlist(prefs, user_prefs)
                suggested_name = suggest_playlist_name(prefs)

                playlist_songs = playlist_result.get("playlist", [])
                if playlist_songs and music_client.spotify and music_client.spotify.is_available():
                    playlist_songs = music_client.enrich_songs(playlist_songs)

                memory.save_playlist(
                    user_id, session_id,
                    suggested_name,
                    playlist_result.get("message", ""),
                    prefs,
                    playlist_songs,
                )

                memory.save_message(user_id, session_id, "assistant", playlist_result["message"])
                if session_id in playlist_sessions:
                    del playlist_sessions[session_id]

                return jsonify({
                    "message": playlist_result["message"],
                    "songs": [],
                    "ask_more": False,
                    "analysis": analysis,
                    "demo_mode": DEMO_MODE,
                    "playlist": {
                        "id": playlist_result["playlist_id"],
                        "songs": playlist_songs,
                        "count": playlist_result["count"],
                        "preferences": playlist_result["preferences"],
                    },
                    "playlist_question": None,
                })

            next_question = playlist_questioner.get_next_question(prefs)
            if next_question:
                question_msg = next_question["question"] + "\n\n"
                for i, opt in enumerate(next_question["options"]):
                    question_msg += f"{i+1}. {opt}\n"
                question_msg += "\nYa da direkt bir mesaj yazabilirsin!"

                playlist_sessions[session_id] = prefs
                memory.save_message(user_id, session_id, "assistant", question_msg)
                return jsonify({
                    "message": question_msg,
                    "songs": [],
                    "ask_more": False,
                    "analysis": analysis,
                    "demo_mode": DEMO_MODE,
                    "playlist": None,
                    "playlist_question": {"key": next_question["key"], "question": next_question["question"], "options": next_question["options"]},
                })

            playlist_result = playlist_generator.generate_playlist(prefs, user_prefs)
            playlist_songs = playlist_result.get("playlist", [])
            if playlist_songs and music_client.spotify and music_client.spotify.is_available():
                playlist_songs = music_client.enrich_songs(playlist_songs)

            memory.save_message(user_id, session_id, "assistant", playlist_result["message"])
            if session_id in playlist_sessions:
                del playlist_sessions[session_id]

            return jsonify({
                "message": playlist_result["message"],
                "songs": [],
                "ask_more": False,
                "analysis": analysis,
                "demo_mode": DEMO_MODE,
                "playlist": {
                    "id": playlist_result["playlist_id"],
                    "songs": playlist_songs,
                    "count": playlist_result["count"],
                    "preferences": playlist_result["preferences"],
                },
                "playlist_question": None,
            })

        llm_response = None
        if not llm_client.demo_mode:
            context = memory.get_context_for_llm(user_id, limit=10)
            analysis_context = {
                "user_message": user_message,
                **analysis,
                "summary": context.get("summary", ""),
            }
            llm_response = llm_client.generate_response(
                context.get("history", []), analysis_context
            )

        api_songs = []
        if not music_client.demo_mode:
            if analysis.get("artist"):
                api_songs = music_client.search_tracks(analysis["artist"], limit=5)
            elif analysis.get("genre"):
                api_songs = music_client.get_recommendations(seed_genres=[analysis["genre"]], limit=5)
            if not api_songs and user_message:
                api_songs = music_client.search_tracks(user_message, limit=5)

        session_key = f"{user_id}:{session_id}"
        conv_state = conversation_states.get(session_key, {})
        current_stage = conv_state.get("stage", "asking_mood")
        session_context = conv_state.get("context", {})

        if llm_response:
            new_stage = conv_state.get("stage", "recommending")
            response_message = llm_response
            response_songs = api_songs if api_songs else []
            ask_more = False
        elif api_songs:
            fallback = response_generator.generate_response(user_message, analysis, user_prefs, stage=current_stage, session_context=session_context)
            response_message = fallback["message"]
            response_songs = api_songs
            ask_more = fallback.get("ask_more", False)
            new_stage = fallback.get("stage", current_stage)
            session_context = fallback.get("context", session_context)
        else:
            fallback = response_generator.generate_response(user_message, analysis, user_prefs, stage=current_stage, session_context=session_context)
            response_message = fallback["message"]
            response_songs = fallback.get("songs", [])
            ask_more = fallback.get("ask_more", False)
            new_stage = fallback.get("stage", current_stage)
            session_context = fallback.get("context", session_context)

        conversation_states[session_key] = {"stage": new_stage, "context": session_context}

        if response_songs and music_client.spotify and music_client.spotify.is_available():
            response_songs = music_client.enrich_songs(response_songs)

        memory.save_message(user_id, session_id, "assistant", response_message)

        return jsonify({
            "message": response_message,
            "songs": response_songs,
            "ask_more": ask_more,
            "analysis": analysis,
            "demo_mode": DEMO_MODE,
            "playlist": None,
            "playlist_question": None,
            "conversation_stage": new_stage,
            "context": session_context,
        })

    except Exception as e:
        logger.error(f"Chat hatasi: {e}", exc_info=True)
        return jsonify({
            "error": str(e),
            "message": "Üzgünüm, bir hata oluştu. Lütfen tekrar dene!",
            "songs": [],
            "ask_more": True,
            "playlist": None,
            "playlist_question": None,
        }), 500


@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "status": "online",
        "demo_mode": DEMO_MODE,
        "music_api": music_client.get_status(),
        "llm_service": llm_client.get_status(),
        "version": "2.1.0",
    })


@app.route("/api/categories", methods=["GET"])
def categories():
    return jsonify({"categories": CATEGORY_LIST})


@app.route("/api/artists", methods=["GET"])
def artists():
    from demo_data import DEMO_SONGS
    artist_map = {}
    for song in DEMO_SONGS:
        artist = song.get("artist", "")
        if not artist:
            continue
        if artist not in artist_map:
            artist_map[artist] = {
                "name": artist,
                "genres": [],
                "moods": [],
                "song_count": 0,
            }
        for g in song.get("genres", []):
            if g not in artist_map[artist]["genres"]:
                artist_map[artist]["genres"].append(g)
        for m in song.get("moods", []):
            if m not in artist_map[artist]["moods"]:
                artist_map[artist]["moods"].append(m)
        artist_map[artist]["song_count"] += 1
    artist_list = sorted(artist_map.values(), key=lambda x: x["song_count"], reverse=True)
    return jsonify({"artists": artist_list})


@app.route("/api/user/<user_id>/preferences", methods=["GET"])
def get_preferences(user_id):
    prefs = memory.get_preferences(user_id)
    return jsonify({"user_id": user_id, "preferences": prefs})


@app.route("/api/user/<user_id>/playlists", methods=["GET"])
def get_playlists(user_id):
    playlists = memory.get_playlists(user_id)
    result = []
    for pl in playlists:
        songs = memory.get_playlist_songs(pl["id"])
        result.append({**pl, "songs": songs})
    return jsonify({"user_id": user_id, "playlists": result})


@app.route("/api/reset/<session_id>", methods=["POST"])
def reset_session(session_id):
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id", session_id)
    memory.clear_conversation(user_id, session_id)
    if session_id in playlist_sessions:
        del playlist_sessions[session_id]
    session_key = f"{user_id}:{session_id}"
    if session_key in conversation_states:
        del conversation_states[session_key]
    return jsonify({"message": "Oturum sıfırlandı.", "session_id": session_id})


@app.route("/api/auth/verify", methods=["POST"])
def auth_verify():
    if not is_firebase_available():
        return jsonify({
            "authenticated": False,
            "error": "Firebase bağlantısı aktif değil. Firebase olmadan da uygulama çalışır.",
            "firebase_available": False,
        }), 200

    data = request.get_json()
    if not data or "id_token" not in data:
        return jsonify({
            "authenticated": False,
            "error": "id_token gerekli.",
            "firebase_available": True,
        }), 400

    user_data = verify_firebase_token(data["id_token"])
    if user_data:
        memory.ensure_user(user_data["uid"], user_data.get("name", ""))
        return jsonify({
            "authenticated": True,
            "user": user_data,
            "firebase_available": True,
        })
    else:
        return jsonify({
            "authenticated": False,
            "error": "Geçersiz veya süresi dolmuş token.",
            "firebase_available": True,
        }), 401


@app.route("/api/auth/status", methods=["GET"])
def auth_status():
    return jsonify({
        "firebase_available": is_firebase_available(),
        "firebase_project_id": os.getenv("FIREBASE_PROJECT_ID", ""),
    })


@app.route("/api/auth/register", methods=["POST"])
def auth_register():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email ve şifre zorunludur."}), 400

    email = data["email"].strip().lower()
    password = data["password"]
    display_name = data.get("display_name", email.split("@")[0])

    if len(password) < 6:
        return jsonify({"error": "Şifre en az 6 karakter olmalıdır."}), 400

    password_hash = _hash_password(password)

    result = memory.register_user(email, password_hash, display_name)
    if not result:
        return jsonify({"error": "Bu email zaten kayıtlı."}), 409

    return jsonify({
        "user": result,
        "message": "Kayıt başarılı!",
    })


@app.route("/api/auth/login", methods=["POST"])
def auth_login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email ve şifre zorunludur."}), 400

    email = data["email"].strip().lower()
    password = data["password"]

    user = memory.get_user_by_email(email)
    if not user:
        return jsonify({"error": "Email veya şifre hatalı."}), 401

    stored_hash = user.get("password_hash", "")
    if not stored_hash:
        return jsonify({"error": "Email veya şifre hatalı."}), 401

    if ":" in stored_hash:
        if not _verify_password(password, stored_hash):
            return jsonify({"error": "Email veya şifre hatalı."}), 401
    else:
        legacy_hash = hashlib.sha256(password.encode()).hexdigest()
        if legacy_hash != stored_hash:
            return jsonify({"error": "Email veya şifre hatalı."}), 401

    return jsonify({"user": {"user_id": user["user_id"], "email": user["email"], "display_name": user["display_name"], "spotify_connected": user.get("spotify_connected", False)}})


@app.route("/api/auth/spotify-link", methods=["POST"])
def spotify_link():
    data = request.get_json()
    if not data or not data.get("user_id") or not data.get("access_token"):
        return jsonify({"error": "user_id ve access_token zorunludur."}), 400

    user_id = data["user_id"]
    access_token = data["access_token"]
    refresh_token = data.get("refresh_token", "")
    expires_at = data.get("expires_at", 0)

    memory.ensure_user(user_id)
    memory.link_spotify(user_id, access_token, refresh_token, expires_at)

    return jsonify({"message": "Spotify hesabı başarıyla bağlandı!", "spotify_connected": True})


@app.route("/api/auth/spotify-unlink", methods=["POST"])
def spotify_unlink():
    data = request.get_json()
    if not data or not data.get("user_id"):
        return jsonify({"error": "user_id zorunludur."}), 400

    memory.unlink_spotify(data["user_id"])
    return jsonify({"message": "Spotify bağlantısı kaldırıldı.", "spotify_connected": False})


@app.route("/api/playlist/<int:playlist_id>", methods=["GET"])
def get_single_playlist(playlist_id):
    playlist = memory.get_playlist_by_id(playlist_id)
    if not playlist:
        return jsonify({"error": "Playlist bulunamadı."}), 404
    songs = memory.get_playlist_songs(playlist_id)
    playlist["songs"] = songs
    return jsonify(playlist)


@app.route("/api/playlist/<int:playlist_id>/rename", methods=["POST"])
def rename_playlist(playlist_id):
    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify({"error": "İsim zorunludur."}), 400
    memory.rename_playlist(playlist_id, data["name"].strip())
    return jsonify({"message": "Playlist ismi güncellendi.", "name": data["name"].strip()})


@app.route("/api/playlist/<int:playlist_id>/delete", methods=["POST"])
def delete_playlist(playlist_id):
    data = request.get_json() or {}
    user_id = data.get("user_id") or None
    memory.delete_playlist(playlist_id, user_id)
    return jsonify({"message": "Playlist silindi."})


@app.route("/api/playlist/suggest-name", methods=["POST"])
def suggest_name():
    data = request.get_json() or {}
    preferences = data.get("preferences", {})
    name = suggest_playlist_name(preferences)
    return jsonify({"name": name})


@app.route("/api/auth/spotify-url", methods=["GET"])
def get_spotify_auth_url():
    client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
    redirect_uri = request.args.get("redirect_uri", "http://localhost:3000/spotify-callback")
    if not client_id:
        return jsonify({"error": "Spotify Client ID ayarlanmamış.", "url": None}), 400

    scopes = "user-read-email user-read-private playlist-modify-public playlist-modify-private playlist-read-private"
    url = (
        f"https://accounts.spotify.com/authorize?response_type=code"
        f"&client_id={client_id}&scope={quote(scopes)}"
        f"&redirect_uri={quote(redirect_uri)}"
    )
    return jsonify({"url": url})


@app.route("/api/auth/spotify-callback", methods=["POST"])
def spotify_callback():
    data = request.get_json()
    if not data or not data.get("code") or not data.get("user_id"):
        return jsonify({"error": "code ve user_id zorunludur."}), 400

    code = data["code"]
    user_id = data["user_id"]
    client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")
    redirect_uri = data.get("redirect_uri", "http://localhost:3000/spotify-callback")

    if not client_id or not client_secret:
        return jsonify({"error": "Spotify API yapılandırması eksik."}), 500

    try:
        import requests as req_lib
        token_response = req_lib.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": redirect_uri,
                "client_id": client_id,
                "client_secret": client_secret,
            },
        )
        token_data = token_response.json()

        if "error" in token_data:
            return jsonify({"error": f"Spotify token hatası: {token_data['error']}"}), 400

        access_token = token_data.get("access_token", "")
        refresh_token = token_data.get("refresh_token", "")
        expires_in = token_data.get("expires_in", 3600)
        import time
        expires_at = time.time() + expires_in

        memory.ensure_user(user_id)
        memory.link_spotify(user_id, access_token, refresh_token, expires_at)

        return jsonify({
            "message": "Spotify hesabı başarıyla bağlandı!",
            "spotify_connected": True,
        })
    except Exception as e:
        logger.error(f"Spotify callback hatası: {e}")
        return jsonify({"error": f"Spotify bağlantı hatası: {str(e)}"}), 500


@app.route("/api/auth/spotify-status", methods=["GET"])
def spotify_status():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id zorunludur."}), 400

    tokens = memory.get_spotify_tokens(user_id)
    connected = bool(tokens and tokens.get("access_token"))

    import time
    if connected and tokens.get("expires_at") and time.time() > tokens["expires_at"]:
        refresh_token = tokens.get("refresh_token", "")
        if refresh_token:
            client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
            client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")
            if client_id and client_secret:
                try:
                    import requests as req_lib
                    refresh_response = req_lib.post(
                        "https://accounts.spotify.com/api/token",
                        data={
                            "grant_type": "refresh_token",
                            "refresh_token": refresh_token,
                            "client_id": client_id,
                            "client_secret": client_secret,
                        },
                    )
                    refresh_data = refresh_response.json()
                    if "access_token" in refresh_data:
                        access_token = refresh_data["access_token"]
                        expires_in = refresh_data.get("expires_in", 3600)
                        expires_at = time.time() + expires_in
                        new_refresh = refresh_data.get("refresh_token", refresh_token)
                        memory.link_spotify(user_id, access_token, new_refresh, expires_at)
                        connected = True
                    else:
                        connected = False
                except Exception:
                    connected = False
            else:
                connected = False
        else:
            connected = False

    return jsonify({"spotify_connected": connected})


@app.route("/api/spotify/export-playlist", methods=["POST"])
def spotify_export_playlist():
    data = request.get_json()
    if not data or not data.get("user_id") or not data.get("playlist_name") or not data.get("songs"):
        return jsonify({"error": "user_id, playlist_name ve songs zorunludur."}), 400

    user_id = data["user_id"]
    playlist_name = data["playlist_name"]
    songs = data["songs"]

    tokens = memory.get_spotify_tokens(user_id)
    if not tokens or not tokens.get("access_token"):
        return jsonify({"error": "Spotify hesabı bağlı değil. Önce Spotify bağlantısı yapmanız gerekiyor."}), 403

    access_token = tokens["access_token"]
    user_spotify = None
    try:
        import spotipy
        user_spotify = spotipy.Spotify(auth=access_token)
        spotify_user = user_spotify.current_user()
        spotify_user_id = spotify_user["id"]
    except Exception as e:
        logger.warning(f"Spotify kullanici bilgisi hatasi: {e}")
        return jsonify({"error": "Spotify token süresi dolmuş veya geçersiz. Tekrar bağlayın."}), 403

    try:
        playlist = user_spotify.user_playlist_create(
            user=spotify_user_id,
            name=playlist_name,
            public=True,
            description=f"DJ AI ile olusturuldu - {len(songs)} sarki",
        )
        playlist_id = playlist["id"]
        track_uris = []
        for song in songs:
            spotify_url = song.get("spotify_url", "")
            if spotify_url and spotify_url != "#none" and "open.spotify.com/track/" in spotify_url:
                track_id = spotify_url.split("/track/")[1].split("?")[0]
                track_uris.append(f"spotify:track:{track_id}")
            elif song.get("name") and song.get("artist"):
                try:
                    search_results = user_spotify.search(q=f"{song['name']} {song['artist']}", type="track", limit=1)
                    items = search_results.get("tracks", {}).get("items", [])
                    if items:
                        track_uris.append(items[0]["uri"])
                except Exception:
                    pass

        if track_uris:
            for i in range(0, len(track_uris), 100):
                user_spotify.user_playlist_add_tracks(
                    user=spotify_user_id,
                    playlist_id=playlist_id,
                    tracks=track_uris[i:i + 100],
                )

        return jsonify({
            "message": f"Playlist '{playlist_name}' Spotify'a aktarildi!",
            "playlist_url": playlist.get("external_urls", {}).get("spotify", ""),
            "track_count": len(track_uris),
            "total_songs": len(songs),
        })
    except Exception as e:
        logger.warning(f"Spotify playlist export hatasi: {e}")
        return jsonify({"error": f"Spotify playlist oluşturma hatası: {str(e)}"}), 500


@app.route("/api/enrich", methods=["POST"])
def enrich_songs():
    data = request.get_json()
    if not data or "songs" not in data:
        return jsonify({"error": "songs alanı zorunludur."}), 400
    songs = data["songs"]
    if not isinstance(songs, list) or len(songs) == 0:
        return jsonify({"error": "songs bir liste olmalıdır."}), 400
    enriched = music_client.enrich_songs(songs)
    return jsonify({"songs": enriched})


@app.route("/api/chat/stream", methods=["POST"])
def chat_stream():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "Mesaj alanı zorunludur."}), 400

        user_message = data["message"].strip()
        session_id = data.get("session_id", "default")
        user_id = data.get("user_id", session_id)

        if not user_message:
            return jsonify({"error": "Mesaj boş olamaz."}), 400

        memory.ensure_user(user_id)
        memory.save_message(user_id, session_id, "user", user_message)
        user_prefs = memory.get_preferences(user_id)
        analysis = analyzer.analyze(user_message)
        analysis["user_id"] = user_id
        memory.update_preferences_from_analysis(user_id, analysis)

        def generate():
            import json as _json
            llm_response = None
            if not llm_client.demo_mode:
                context = memory.get_context_for_llm(user_id, limit=10)
                analysis_context = {
                    "user_message": user_message,
                    **analysis,
                    "summary": context.get("summary", ""),
                }
                stream = llm_client.generate_response_stream(
                    context.get("history", []), analysis_context
                )
                if stream:
                    full_response = ""
                    for token in stream:
                        if isinstance(token, str):
                            full_response += token
                            yield f"data: {_json.dumps({'type': 'token', 'content': token})}\n\n"
                    yield f"data: {_json.dumps({'type': 'done', 'full_response': full_response})}\n\n"
                    memory.save_message(user_id, session_id, "assistant", full_response)
                    return

            fallback = response_generator.generate_response(user_message, analysis, user_prefs)
            response_message = fallback["message"]
            yield f"data: {_json.dumps({'type': 'token', 'content': response_message})}\n\n"
            yield f"data: {_json.dumps({'type': 'done', 'full_response': response_message})}\n\n"
            memory.save_message(user_id, session_id, "assistant", response_message)

        return Response(
            stream_with_context(generate()),
            mimetype="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "X-Accel-Buffering": "no",
                "Connection": "keep-alive",
            },
        )

    except Exception as e:
        logger.error(f"Stream chat hatasi: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    port = int(os.getenv("PORT", 5000))
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"

    print("=" * 50)
    print("DJ AI v2.1 - Muzik Oneri Chatbot")
    print("=" * 50)
    print(f"Sunucu: http://localhost:{port}")
    print(f"Demo Modu: {'AKTIF' if DEMO_MODE else 'KAPALI'}")
    print(f"Muzik API: {music_client.get_status()}")
    print(f"LLM Servisi: {llm_client.get_status()}")
    print(f"Veritabani: {memory.db_path}")
    print(f"Firebase: {'AKTIF' if is_firebase_available() else 'KAPALI (SQLite modu)'}")
    print("=" * 50)

    app.run(host="0.0.0.0", port=port, debug=debug_mode, use_reloader=False)


def serve_production(host="0.0.0.0", port=5000):
    try:
        from waitress import serve as waitress_serve
    except ImportError:
        print("HATA: waitress yuklu degil. 'pip install waitress' ile yukleyin.")
        sys.exit(1)

    print("=" * 50)
    print("DJ AI v2.1 - PRODUCTION (Waitress)")
    print("=" * 50)
    print(f"Sunucu: http://{host}:{port}")
    print(f"Demo Modu: {'AKTIF' if DEMO_MODE else 'KAPALI'}")
    print(f"Muzik API: {music_client.get_status()}")
    print(f"LLM Servisi: {llm_client.get_status()}")
    print(f"Veritabani: {memory.db_path}")
    print(f"Firebase: {'AKTIF' if is_firebase_available() else 'KAPALI (SQLite modu)'}")
    print("=" * 50)

    waitress_serve(app, host=host, port=port, threads=4)