import random
import re
from demo_data import DEMO_SONGS, GENRE_LABELS, MOOD_LABELS, ACTIVITY_LABELS


MOOD_TO_GENRE_MAP = {
    "mutlu": ["pop", "turkce_pop", "funk", "disko", "soul"],
    "uzgun": ["blues", "arabesk", "turkce_rock", "klasik", "jazz", "damar"],
    "enerjik": ["rock", "rap", "elektronik", "edm", "metal", "turkce_rock", "punk"],
    "romantik": ["pop", "rnb", "jazz", "klasik", "soul", "folk"],
    "asik": ["pop", "rnb", "soul", "klasik", "turkce_pop"],
    "sakin": ["lofi", "klasik", "jazz", "ambient", "blues", "neoklasik"],
    "motivasyon": ["rock", "rap", "elektronik", "edm", "turkce_rock", "metal"],
    "sinirli": ["rock", "metal", "grunge", "punk", "rap"],
    "melankolik": ["blues", "arabesk", "klasik", "turkce_rock", "indie", "lofi"],
    "nostaljik": ["rock", "turkce_rock", "arabesk", "jazz", "anadolu_rock", "thm"],
    "guclu": ["metal", "rap", "rock", "elektronik", "edm"],
    "epik": ["rock", "klasik", "elektronik", "neoklasik"],
}

ACTIVITY_TO_GENRE_MAP = {
    "ders": ["lofi", "klasik", "jazz", "ambient", "neoklasik"],
    "spor": ["rock", "rap", "turkce_rap", "elektronik", "edm", "metal", "turkce_rock"],
    "gece": ["jazz", "blues", "lofi", "elektronik", "rnb", "indie"],
    "yolculuk": ["rock", "pop", "turkce_rock", "indie", "turkce_pop", "anadolu_rock"],
    "uyku": ["lofi", "ambient", "klasik", "neoklasik"],
    "parti": ["pop", "elektronik", "edm", "rap", "funk", "disko", "reggaeton"],
    "kahve": ["jazz", "lofi", "soul", "folk", "blues"],
    "yagmur": ["blues", "lofi", "jazz", "klasik", "indie", "folk"],
    "yazlik": ["pop", "reggaeton", "elektronik", "turkce_pop", "funk"],
    "kislik": ["klasik", "jazz", "lofi", "folk", "blues"],
    "sabah": ["pop", "folk", "jazz", "soul", "funk"],
    "kosu": ["rap", "elektronik", "edm", "rock", "turkce_rap"],
    "araba": ["rock", "pop", "turkce_rock", "indie", "elektronik", "anadolu_rock"],
    "oyun": ["elektronik", "edm", "rock", "rap", "metal"],
    "kod": ["lofi", "elektronik", "ambient", "house", "jazz"],
    "yayin": ["rap", "elektronik", "pop", "rock"],
    "chill": ["lofi", "jazz", "rnb", "indie", "ambient"],
    "odak": ["lofi", "klasik", "ambient", "neoklasik"],
    "meditasyon": ["ambient", "klasik", "neoklasik", "lofi"],
}


class PlaylistGenerator:
    def __init__(self, songs_db=None):
        self.songs_db = songs_db or DEMO_SONGS

    def is_playlist_request(self, message):
        text = message.lower().strip()
        strict_indicators = [
            "playlist", "liste yap", "listesi", "liste olustur", "liste ver",
            "karisik liste", "karma liste", "karisik playlist",
            "sarki listesi", "muzik listesi",
            "sarkilik liste", "parca listesi",
            "olustur", "palylist",
        ]
        count_pattern = r"(\d+)\s*(sarki|parca|tur|sanatci)\s*(liste|listesi|playlist|karisik|karma)"
        if any(ind in text for ind in strict_indicators):
            return True
        if re.search(count_pattern, text):
            return True
        return False

    def detect_preferences(self, message, analysis=None):
        prefs = {
            "genres": [],
            "mood": None,
            "activity": None,
            "artist": None,
            "language": None,
            "count": 10,
            "energy": None,
        }

        if analysis:
            if analysis.get("genres") and len(analysis["genres"]) > 0:
                prefs["genres"] = analysis["genres"]
            elif analysis.get("genre"):
                prefs["genres"] = [analysis["genre"]]
            if analysis.get("mood"):
                prefs["mood"] = analysis["mood"]
            if analysis.get("activity"):
                prefs["activity"] = analysis["activity"]
            if analysis.get("artist"):
                prefs["artist"] = analysis["artist"]
            if analysis.get("language"):
                prefs["language"] = analysis["language"]

        text_norm = message.lower().strip()
        for tr_char, en_char in {"ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u"}.items():
            text_norm = text_norm.replace(tr_char, en_char)

        count_match = re.search(r"(\d+)\s*(sarki|parca|tur|sanatci|sarkilik)", text_norm)
        if count_match:
            prefs["count"] = min(int(count_match.group(1)), 30)

        energy_keywords = {
            "yuksek": ["yuksek", "yuksek enerji", "enerjik", "sert", "hizli", "agir", "guc", "guc"],
            "dusuk": ["dusuk", "sakin", "yavas", "rahat", "huzur", "dinlendirici"],
        }
        for energy, words in energy_keywords.items():
            if any(w in text_norm for w in words):
                prefs["energy"] = energy

        return prefs

    def generate_playlist(self, preferences, user_prefs=None):
        genres = preferences.get("genres", [])
        mood = preferences.get("mood")
        activity = preferences.get("activity")
        artist = preferences.get("artist")
        language = preferences.get("language")
        count = min(preferences.get("count", 10), 30)
        energy = preferences.get("energy")

        target_genres = list(genres)
        if mood and mood in MOOD_TO_GENRE_MAP:
            for g in MOOD_TO_GENRE_MAP[mood]:
                if g not in target_genres:
                    target_genres.append(g)
        if activity and activity in ACTIVITY_TO_GENRE_MAP:
            for g in ACTIVITY_TO_GENRE_MAP[activity]:
                if g not in target_genres:
                    target_genres.append(g)

        if user_prefs:
            for g in user_prefs.get("liked_genres", []):
                if g not in target_genres:
                    target_genres.append(g)

        if not target_genres:
            target_genres = ["pop", "rock"]

        if energy == "dusuk":
            target_genres = [g for g in target_genres if g not in ["metal", "rap", "rock", "elektronik"]]
            for g in ["lofi", "ambient", "klasik", "jazz"]:
                if g not in target_genres:
                    target_genres.append(g)
        elif energy == "yuksek":
            target_genres = [g for g in target_genres if g not in ["lofi", "ambient", "klasik", "jazz"]]
            for g in ["rock", "rap", "elektronik"]:
                if g not in target_genres:
                    target_genres.append(g)

        filtered_songs = []
        for song in self.songs_db:
            score = 0
            song_genres = song.get("genres", [])
            song_moods = song.get("moods", [])
            song_activities = song.get("activities", [])

            genre_overlap = set(song_genres) & set(target_genres)
            if genre_overlap:
                score += len(genre_overlap) * 3

            if mood and mood in song_moods:
                score += 2
            if activity and activity in song_activities:
                score += 2
            if artist and song.get("artist", "").lower() == artist.lower():
                score += 5

            if language:
                if language == "tr" and song.get("language") == "tr":
                    score += 1
                elif language == "en" and song.get("language") == "en":
                    score += 1

            if user_prefs:
                disliked = user_prefs.get("disliked_genres", [])
                if any(g in disliked for g in song_genres):
                    score -= 5

            if score > 0:
                filtered_songs.append((score, song))

        filtered_songs.sort(key=lambda x: x[0], reverse=True)

        seen_names = set()
        unique_songs = []
        for score, song in filtered_songs:
            name_key = f"{song['name']}_{song['artist']}"
            if name_key not in seen_names:
                seen_names.add(name_key)
                unique_songs.append(song)

        score_cutoff = filtered_songs[0][0] if filtered_songs else 0
        if score_cutoff > 0:
            high_score = [s for s in unique_songs if any(
                g in target_genres for g in s.get("genres", [])
            )]
            low_score = [s for s in unique_songs if not any(
                g in target_genres for g in s.get("genres", [])
            )]
            random.shuffle(high_score)
            random.shuffle(low_score)
            unique_songs = high_score + low_score

        if len(unique_songs) < count:
            same_genre_remaining = [
                s for s in self.songs_db
                if f"{s['name']}_{s['artist']}" not in seen_names
                and any(g in s.get("genres", []) for g in target_genres)
            ]
            random.shuffle(same_genre_remaining)
            unique_songs.extend(same_genre_remaining)
            if len(unique_songs) < count:
                other_remaining = [
                    s for s in self.songs_db
                    if f"{s['name']}_{s['artist']}" not in seen_names
                    and f"{s['name']}_{s['artist']}" not in {f"{x['name']}_{x['artist']}" for x in unique_songs}
                ]
                random.shuffle(other_remaining)
                unique_songs.extend(other_remaining)

        selected = unique_songs[:count]

        genre_distribution = {}
        for song in selected:
            for g in song.get("genres", []):
                genre_distribution[g] = genre_distribution.get(g, 0) + 1

        playlist_description = self._generate_description(preferences, genre_distribution)

        return {
            "playlist_id": f"pl_{random.randint(10000, 99999)}",
            "message": playlist_description,
            "playlist": [
                {
                    "name": s.get("name", ""),
                    "artist": s.get("artist", ""),
                    "album": s.get("album", ""),
                    "genres": s.get("genres", []),
                    "genre": s.get("genres", [""])[0] if s.get("genres") else "",
                    "genre_label": GENRE_LABELS.get(s.get("genres", [""])[0], "") if s.get("genres") else "",
                    "mood": s.get("moods", [""])[0] if s.get("moods") else "",
                    "moods": s.get("moods", []),
                    "language": s.get("language", ""),
                    "cover_url": s.get("cover_url", ""),
                    "spotify_url": s.get("spotify_url", ""),
                    "reason": s.get("reason", ""),
                    "duration": s.get("duration", ""),
                }
            for s in selected
            ],
            "count": len(selected),
            "preferences": preferences,
        }

    def _generate_description(self, prefs, genre_dist):
        parts = []
        if prefs.get("mood"):
            mood_label = MOOD_LABELS.get(prefs["mood"], prefs["mood"])
            parts.append(f"{mood_label} ruh haline")
        if prefs.get("activity"):
            act_label = ACTIVITY_LABELS.get(prefs["activity"], prefs["activity"])
            parts.append(f"{act_label} durumuna")
        if prefs.get("genres"):
            genre_labels = [GENRE_LABELS.get(g, g) for g in prefs["genres"][:3]]
            parts.append(f"{', '.join(genre_labels)} turunde")

        if parts:
            desc = f" {' ve '.join(parts)} uygun playlistini hazirladim!"
        else:
            desc = "Sana ozel bir playlist hazirladim!"

        if genre_dist:
            top_genres = sorted(genre_dist.items(), key=lambda x: x[1], reverse=True)[:3]
            genre_str = ", ".join([f"{GENRE_LABELS.get(g, g)} ({c})" for g, c in top_genres])
            desc += f"\n\nPlaylist iceriginde {genre_str} agirlikli."

        desc += f"\n\nToplam {prefs.get('count', 10)} sarkilik liste. Hadi dinlemeye basla! 🎶"
        return desc


class PlaylistQuestioner:
    def __init__(self):
        self.questions = [
            {
                "key": "count",
                "question": "Playlist kac sarkilik olsun?",
                "options": ["5 sarki (kisa)", "10 sarki (orta)", "15 sarki (uzun)", "20 sarki (detayli)"],
                "values": [5, 10, 15, 20],
            },
            {
                "key": "energy",
                "question": "Playlist enerjisi nasil olsun?",
                "options": ["Yuksek enerji (sert, hizli)", "Orta enerji (dengeli)", "Dusuk enerji (sakin, rahat)"],
                "values": ["yuksek", "orta", "dusuk"],
            },
            {
                "key": "language",
                "question": "Dil tercihin ne?",
                "options": ["Sadece Turkce", "Sadece Yabanci", "Karisik (Turkce + Yabanci)"],
                "values": ["tr", "en", "mixed"],
            },
        ]

    def get_next_question(self, prefs):
        for q in self.questions:
            if prefs.get(q["key"]) is None:
                return q
        return None

    def parse_answer(self, question_key, answer):
        text = answer.lower().strip()
        for tr_char, en_char in {"ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u"}.items():
            text = text.replace(tr_char, en_char)

        if question_key == "count":
            count_match = re.search(r"(\d+)", text)
            if count_match:
                return min(int(count_match.group(1)), 30)
            if any(w in text for w in ["kisa", "az", "biraz"]):
                return 5
            if any(w in text for w in ["orta", "normal", "fena"]):
                return 10
            if any(w in text for w in ["cok uzun", "long"]):
                return 20
            if any(w in text for w in ["uzun", "detayli", "cok"]):
                return 15
            return 10

        elif question_key == "energy":
            if any(w in text for w in ["yuksek", "enerjik", "sert", "hizli", "agir"]):
                return "yuksek"
            if any(w in text for w in ["dusuk", "sakin", "yavas", "rahat", "huzur"]):
                return "dusuk"
            return "orta"

        elif question_key == "language":
            if any(w in text for w in ["turkce", "turk", "yerli"]):
                return "tr"
            if any(w in text for w in ["yabanci", "ingilizce", "english"]):
                return "en"
            return "mixed"

        return None