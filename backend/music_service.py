import os
import time
import logging
from abc import ABC, abstractmethod
from demo_data import DEMO_SONGS, GENRE_LABELS

logger = logging.getLogger(__name__)


class MusicService(ABC):
    @abstractmethod
    def search_tracks(self, query, limit=5):
        pass

    @abstractmethod
    def get_recommendations(self, seed_genres=None, seed_artists=None, limit=5):
        pass

    @abstractmethod
    def is_available(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


class SpotifyService(MusicService):
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")
        self._token = None
        self._token_expires = time.time() + 3600
        self.sp = None
        self._available = False
        if self.client_id and self.client_secret:
            try:
                import spotipy
                from spotipy.oauth2 import SpotifyClientCredentials
                auth_manager = SpotifyClientCredentials(
                    client_id=self.client_id,
                    client_secret=self.client_secret,
                )
                self.sp = spotipy.Spotify(auth_manager=auth_manager)
                self.sp.search("test", limit=1)
                self._available = True
                logger.info("Spotify API baglantisi basarili")
            except Exception as e:
                logger.warning(f"Spotify API baglantisi basarisiz: {e}")
                self._available = False

    def _refresh_token(self):
        try:
            import spotipy
            from spotipy.oauth2 import SpotifyClientCredentials
            auth_manager = SpotifyClientCredentials(
                client_id=self.client_id,
                client_secret=self.client_secret,
            )
            self.sp = spotipy.Spotify(auth_manager=auth_manager)
            self._token_expires = time.time() + 3600
        except Exception as e:
            logger.warning(f"Spotify token yenileme hatasi: {e}")
            self._available = False

    def is_available(self):
        if not self._available:
            return False
        if time.time() > self._token_expires:
            self._refresh_token()
        return self._available

    def search_tracks(self, query, limit=5):
        if not self.is_available():
            return []
        try:
            results = self.sp.search(q=query, type="track", limit=limit)
            tracks = []
            for item in results.get("tracks", {}).get("items", []):
                track = {
                    "name": item.get("name", ""),
                    "artist": item["artists"][0]["name"] if item.get("artists") else "",
                    "album": item.get("album", {}).get("name", ""),
                    "cover_url": item.get("album", {}).get("images", [{}])[0].get("url", "") if item.get("album", {}).get("images") else "",
                    "spotify_url": item.get("external_urls", {}).get("spotify", ""),
                    "duration_ms": item.get("duration_ms", 0),
                    "genre": "",
                    "genre_label": "",
                    "mood": "",
                    "language": "",
                    "reason": "Spotify arama sonucu",
                }
                tracks.append(track)
            return tracks
        except Exception as e:
            logger.warning(f"Spotify arama hatasi: {e}")
            self._available = False
            return []

    def get_recommendations(self, seed_genres=None, seed_artists=None, limit=5):
        if not self.is_available():
            return []
        try:
            kwargs = {"limit": limit}
            if seed_genres:
                kwargs["seed_genres"] = seed_genres[:5]
            if seed_artists:
                kwargs["seed_artists"] = seed_artists[:5]
            if not seed_genres and not seed_artists:
                kwargs["seed_genres"] = ["pop"]
            results = self.sp.recommendations(**kwargs)
            tracks = []
            for item in results.get("tracks", []):
                track = {
                    "name": item.get("name", ""),
                    "artist": item["artists"][0]["name"] if item.get("artists") else "",
                    "album": item.get("album", {}).get("name", ""),
                    "cover_url": item.get("album", {}).get("images", [{}])[0].get("url", "") if item.get("album", {}).get("images") else "",
                    "spotify_url": item.get("external_urls", {}).get("spotify", ""),
                    "duration_ms": item.get("duration_ms", 0),
                    "genre": "",
                    "genre_label": "",
                    "mood": "",
                    "language": "",
                    "reason": "Spotify oneri",
                }
                tracks.append(track)
            return tracks
        except Exception as e:
            logger.warning(f"Spotify oneri hatasi: {e}")
            return []

    def get_status(self):
        return {"available": self._available, "name": "Spotify"}


class DemoMusicService(MusicService):
    def __init__(self):
        self.songs = DEMO_SONGS

    def is_available(self):
        return True

    def search_tracks(self, query, limit=5):
        from analyzer import MessageAnalyzer
        analyzer = MessageAnalyzer()
        analysis = analyzer.analyze(query)
        genre = analysis.get("genre")
        mood = analysis.get("mood")
        activity = analysis.get("activity")
        artist = analysis.get("artist")
        return self._select_songs(genre, mood, activity, artist, limit)

    def get_recommendations(self, seed_genres=None, seed_artists=None, limit=5):
        genre = seed_genres[0] if seed_genres else None
        return self._select_songs(genre=genre, count=limit)

    def _select_songs(self, genre=None, mood=None, activity=None, artist=None, language=None, count=5):
        import random
        candidates = list(self.songs)
        scored = []
        for song in candidates:
            score = 0
            if genre and genre in song.get("genres", []):
                score += 3
            if mood and mood in song.get("moods", []):
                score += 2
            if activity and activity in song.get("activities", []):
                score += 2
            if artist and song.get("artist", "").lower() == artist.lower():
                score += 5
            if language:
                if song.get("language") == language:
                    score += 1
            scored.append((score, song))
        scored.sort(key=lambda x: x[0], reverse=True)
        top = [s for sc, s in scored if sc > 0]
        if len(top) < count:
            remaining = [s for sc, s in scored if sc == 0]
            random.shuffle(remaining)
            top.extend(remaining)
        result = top[:count]
        return [
            {
                "name": s.get("name", ""),
                "artist": s.get("artist", ""),
                "album": s.get("album", ""),
                "genre": s.get("genres", [""])[0] if s.get("genres") else "",
                "genre_label": GENRE_LABELS.get(s.get("genres", [""])[0], "") if s.get("genres") else "",
                "mood": s.get("moods", [""])[0] if s.get("moods") else "",
                "language": s.get("language", ""),
                "cover_url": s.get("cover_url", ""),
                "spotify_url": s.get("spotify_url", ""),
                "reason": s.get("reason", ""),
                "duration": s.get("duration", ""),
            }
            for s in result
        ]

    def get_status(self):
        return {"available": True, "name": "Demo", "song_count": len(self.songs)}


class MusicClient:
    def __init__(self):
        self.spotify = None
        self.demo = DemoMusicService()
        self.demo_mode = True
        self._init_spotify()

    def _init_spotify(self):
        client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")
        if client_id and client_secret:
            try:
                self.spotify = SpotifyService()
                if self.spotify.is_available():
                    self.demo_mode = False
                    logger.info("Spotify servisi aktif")
            except Exception as e:
                logger.warning(f"Spotify baslatma hatasi: {e}")
                self.spotify = None

    def search_tracks(self, query, limit=5):
        if self.spotify and self.spotify.is_available():
            result = self.spotify.search_tracks(query, limit)
            if result:
                return result
        return self.demo.search_tracks(query, limit)

    def get_recommendations(self, seed_genres=None, seed_artists=None, limit=5):
        if self.spotify and self.spotify.is_available():
            result = self.spotify.get_recommendations(seed_genres, seed_artists, limit)
            if result:
                return result
        return self.demo.get_recommendations(seed_genres, seed_artists, limit)

    def enrich_songs(self, songs):
        if not self.spotify or not self.spotify.is_available():
            return songs
        enriched = []
        for song in songs:
            if song.get("cover_url") and song.get("spotify_url") and song.get("spotify_url") != "#none":
                enriched.append(song)
                continue
            try:
                query = f"{song.get('name', '')} {song.get('artist', '')}"
                results = self.spotify.search_tracks(query, limit=1)
                if results and len(results) > 0:
                    spotify_track = results[0]
                    enriched_song = {**song}
                    if spotify_track.get("cover_url"):
                        enriched_song["cover_url"] = spotify_track["cover_url"]
                    if spotify_track.get("spotify_url") and spotify_track["spotify_url"] != "#none":
                        enriched_song["spotify_url"] = spotify_track["spotify_url"]
                    if not enriched_song.get("album") and spotify_track.get("album"):
                        enriched_song["album"] = spotify_track["album"]
                    enriched.append(enriched_song)
                else:
                    enriched.append(song)
            except Exception as e:
                logger.warning(f"Sarki zenginlestirme hatasi ({song.get('name')}): {e}")
                enriched.append(song)
        return enriched

    def get_status(self):
        status = {
            "demo_mode": self.demo_mode,
            "spotify": self.spotify.get_status() if self.spotify else {"available": False, "name": "Spotify"},
            "demo": self.demo.get_status(),
        }
        return status