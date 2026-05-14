import re
from demo_data import DEMO_SONGS, GENRE_LABELS, MOOD_LABELS, ACTIVITY_LABELS

TURKISH_REPLACEMENTS = {
    "ç": "c", "Ç": "C", "ğ": "g", "Ğ": "G", "ı": "i",
    "İ": "I", "ö": "o", "Ö": "O", "ş": "s", "Ş": "S",
    "ü": "u", "Ü": "U",
}

GENRE_KEYWORDS = {
    "rock": ["rock", "rok", "rokcu", "rockci", "gitar", "gitarist", "rok muzik", "gitar solo", "rock and roll"],
    "pop": ["pop", "popcu", "pop sarki", "pop muzik", "pop sarkilari", "pop muzigi"],
    "rap": ["rap", "rapci", "hiphop", "hip-hop", "hip hop", "rap muzik", "trap muzik", "rap sarki", "rap sarkilari"],
    "trap": ["trap", "trap muzik", "trapci", "trap sarki"],
    "jazz": ["jazz", "caz", "jazz muzik", "caz muzigi"],
    "blues": ["blues", "bluz", "mavi muzik", "blues muzik"],
    "klasik": ["klasik", "klasik muzik", "piyano", "senfoni", "orkestra", "bach", "mozart", "beethoven", "chopin", "vivaldi", "debussy", "yiruma", "klasik piyano"],
    "metal": ["metal", "heavy metal", "metalci", "metal muzik", "thrash"],
    "punk": ["punk", "punk rock", "punkci"],
    "indie": ["indie", "indi", "alternatif", "alternatif rock", "indie rock", "indie pop"],
    "alternatif_rock": ["alternatif rock", "alt rock", "alternatif rok"],
    "elektronik": ["elektronik", "elektronik muzik", "edm", "techno", "house", "dj", "dans muzigi", "synth"],
    "edm": ["edm", "electronic dance", "festival muzigi", "edm muzik"],
    "house": ["house", "house muzik", "deep house"],
    "techno": ["techno", "techno muzik"],
    "lofi": ["lofi", "lo-fi", "lo fi", "chillhop", "chill hop", "ders muzigi", "calisma muzigi", "lo-fi muzik"],
    "ambient": ["ambient", "ambient muzik", "meditasyon muzigi"],
    "reggaeton": ["reggaeton", "regaton", "latin", "latin muzik"],
    "country": ["country", "country muzik"],
    "folk": ["folk", "folk muzik", "halk muzigi", "folk sarki"],
    "soul": ["soul", "soul muzik", "neosoul", "neo-soul"],
    "funk": ["funk", "funkci", "funk muzik", "funk sarki"],
    "disko": ["disko", "disco", "disko muzik", "dance muzik", "disko sarki"],
    "rnb": ["rnb", "r&b", "r and b", "rnb muzik", "rnb sarki"],
    "turkce_pop": ["turkce pop", "turk pop", "yerli pop", "turkce sarki", "yerli sarki", "turk popu", "turkce sarkilar", "turkce hit", "yerli muzik"],
    "turkce_rap": ["turkce rap", "turk rap", "yerli rap", "turkce hiphop", "turk rapci", "turkce rap sarkilari"],
    "arabesk": ["arabesk", "arabesk sarki", "arabesk muzik", "kirtlac", "turk sanat", "arabesk sarkilar", "damar sarki"],
    "anadolu_rock": ["anadolu rock", "anadolu rok", "baris manco", "cem karaca", "anadolu", "anadolu rock sarki", "turkce rock sarkilari"],
    "turkce_rock": ["turkce rock", "turk rok", "turkce rok", "yerli rock", "turkce rock sarkilari"],
    "thm": ["halk muzigi", "halk", "turk halk", "turlu", "zurna", "davul", "baglama", "halk turkusu", "thm", "türk halk müziği", "halk sarkisi"],
    "tsm": ["sanat muzigi", "tsm", "turk sanat muzigi", "klasik turk", "makam", "sanat sarkisi"],
    "karadeniz": ["karadeniz", "laz", "horon", "karadeniz muzigi", "kemence", "karadeniz sarkisi"],
    "fantazi": ["fantazi", "fantazi muzik", "turk fantazi"],
    "damar": ["damar", "damar sarki", "acili", "firtali", "damar sarkilar", "canim yandi", "uzgun sarki"],
    "oyun_havasi": ["oyun havasi", "oyun", "zeybek", "halay", "kolbasti", "oyun muzigi"],
    "neoklasik": ["neoklasik", "neo klasik", "modern klasik", "neoklasik muzik"],
    "psychedelik": ["psychedelik", "psikedelik", "psychedelic", "psychedelik rock"],
    "grunge": ["grunge", "grunge rock", "grunge muzik"],
    "synthpop": ["synth", "synthpop", "synth pop", "synthwave", "synth muzik"],
    "hiphop": ["hiphop", "hip-hop", "hip hop", "hiphop muzik"],
}

MOOD_KEYWORDS = {
    "mutlu": ["mutlu", "mutluyum", "neseli", "nese", "sevinc", "keyifli", "eglenceli", "guzel", "happy", "iyi", "iyiyim", "harika", "super", "muhtesem", "keyifliyim", "neşeliyim", "guzel bir gun", "iyi hissediyorum", "mutluyum"],
    "uzgun": ["uzgun", "uzgunum", "mutsuz", "aglamak", "huzun", "huzunlu", "kederli", "moralim bozuk", "moral bozuk", "depresif", "melankoli", "uzuntu", "aci", "dertli", "canim sikildi", "mutsuzum", "kotuyum", "kotu hissediyorum", "uzgun hissediyorum"],
    "asik": ["asik", "ask", "sevgi", "sevda", "sevgili", "gonul", "flort", "seviyorum", "askim", "sevgilim", "yuregim", "kalbim", "asigim", "askta"],
    "enerjik": ["enerjik", "enerji", "canli", "dinamik", "guclu", "coskulu", "atesli", "hizli", "tempo", "aktif", "enerjik hissediyorum", "canliyim", "enerji dolu"],
    "sakin": ["sakin", "rahat", "dinlen", "sessiz", "huzur", "huzurlu", "yumusak", "dinlendir", "sukunet", "dingin", "rahatlat", "sakinim", "rahatliyorum"],
    "motivasyon": ["motivasyon", "cesaret", "basari", "hedef", "gaz", "motive", "inspirasyon", "motive olmam lazim", "gaza ihtiyacim var"],
    "sinirli": ["sinirli", "sinir", "ofkeli", "ofke", "kizgin", "gergin", "stresli", "stres", "bunalmis", "sinirlenme", "sinirliyim", "stresliyim"],
    "melankolik": ["melankolik", "melankoli", "duygusal", "huzunlu", "gozyasi", "icli", "kederli", "duygusalim", "huzunluyum"],
    "nostaljik": ["nostalj", "nostaljik", "eski", "gecmis", "hatira", "ani", "eskiden", "cocukluk", "gecmisi", "eskileri ozledim", "nostaljik hissediyorum"],
    "romantik": ["romantik", "romantizm", "sevgi dolu", "sefkatli", "romantik muzik", "romantik hissediyorum"],
    "guclu": ["guclu", "guc", "kuvvetli", "dayanikli", "sert", "guclu hissediyorum"],
    "epik": ["epik", "efsane", "devasa", "muhtesem", "epik muzik"],
    "yorgun": ["yorgun", "yorgunum", "bitkin", "bittim", "tükendim", "yorgun hissediyorum", "bitkinim", "tükenmis", "exhausted", "tired"],
}

ACTIVITY_KEYWORDS = {
    "ders": ["ders", "calisma", "calis", "ogren", "okul", "universite", "sinav", "odaklan", "konsantrasyon", "kitap", "okuma", "study", "odev"],
    "spor": ["spor", "egzersiz", "antrenman", "kosu", "fitness", "gym", "spor salonu", "yuruyus", "bisiklet", "hareket", "cardio", "agirlik"],
    "gece": ["gece", "gece vakti", "geceyi", "gece olmus", "uyku tumuyor", "gececi", "late night", "midnight", "gece hayati"],
    "yolculuk": ["yolculuk", "yol", "seyahat", "tatil", "araba", "ucak", "otobus", "tren", "karayolu", "yolda", "road trip"],
    "uyku": ["uyku", "uyumak", "uyu", "dinlen", "rahatla", "yoga", "sakinles", "sleep", "insomnia", "yatmadan"],
    "parti": ["parti", "eglence", "dans", "disco", "disko", "club", "partiye", "kutlama", "dogum gunu", "kutla"],
    "kahve": ["kahve", "kahvalti", "kafede", "cay", "cay icin", "breakfast"],
    "yagmur": ["yagmur", "yagmurlu", "yagmurlu hava", "firtina", "yagmurda", "yagmurlu gun"],
    "yazlik": ["yaz", "yazlik", "tatil", "plaj", "deniz", "havuz", "yaz gunu", "gunes"],
    "kislik": ["kis", "kislik", "kis gunu", "kar", "karda", "soguk", "sicak muzik"],
    "sabah": ["sabah", "sabah muzigi", "uyanma", "gunaydin", "morning", "baslangic"],
    "kosu": ["kosu", "kosmak", "jogging", "kosu muzigi", "yuruyus", "yurume"],
    "oyun": ["oyun", "oyun muzigi", "espor", "gaming", "oyun oynarken"],
    "kod": ["kod", "kod yazma", "programlama", "yazilim", "developer", "coding", "hack"],
    "chill": ["chill", "sakin", "rahat", "gece chill", "chill muzik", "chill out"],
    "odak": ["odaklan", "odak", "konsantre", "focus", "dikkat", "verimli"],
    "meditasyon": ["meditasyon", "meditation", "mindfulness", "nefes", "zihin"],
}

ARTIST_KEYWORDS = {
    "Queen": ["queen", "freddie", "mercury"],
    "Eminem": ["eminem", "marshall", "mathers", "slim shady"],
    "Sezen Aksu": ["sezen", "sezen aksu"],
    "Tarkan": ["tarkan"],
    "Duman": ["duman"],
    "Mor ve Otesi": ["mor ve otesi", "mor ve ozgese"],
    "Sebnem Ferah": ["sebnem", "ferah", "sebnem ferah"],
    "Adele": ["adele"],
    "Ed Sheeran": ["ed sheeran", "sheeran"],
    "The Weeknd": ["the weeknd", "weeknd"],
    "Coldplay": ["coldplay", "chris martin"],
    "Imagine Dragons": ["imagine dragons", "imagine"],
    "Metallica": ["metallica"],
    "Baris Manco": ["baris manco", "baris manco"],
    "Kendrick Lamar": ["kendrick", "kendrick lamar"],
    "Daft Punk": ["daft punk", "daft"],
    "Avicii": ["avicii"],
    "Miles Davis": ["miles davis", "miles"],
    "Pink Floyd": ["pink floyd"],
    "Nirvana": ["nirvana", "kurt cobain"],
    "Arctic Monkeys": ["arctic monkeys", "arctic"],
    "Tame Impala": ["tame impala"],
    "Muslum Gurses": ["muslum", "muslum gurses", "gurses"],
    "Ibrahim Tatlises": ["ibrahim tatlises", "tatlises", "ibrahim"],
    "AC/DC": ["acdc", "ac/dc", "angus young"],
    "Led Zeppelin": ["led zeppelin", "led zep"],
    "The Beatles": ["beatles", "the beatles"],
    "Iron Maiden": ["iron maiden"],
    "Black Sabbath": ["black sabbath", "sabbath", "ozzy"],
    "Green Day": ["green day", "billie joe"],
    "Radiohead": ["radiohead", "thom yorke"],
    "Drake": ["drake"],
    "Travis Scott": ["travis scott", "travis"],
    "Macklemore": ["macklemore"],
    "Kanye West": ["kanye", "kanye west", "ye"],
    "Louis Armstrong": ["louis armstrong"],
    "Dave Brubeck": ["dave brubeck", "brubeck"],
    "Debussy": ["debussy", "claude debussy"],
    "Beethoven": ["beethoven"],
    "Vivaldi": ["vivaldi"],
    "Yiruma": ["yiruma"],
    "John Legend": ["john legend"],
    "Harry Styles": ["harry styles"],
    "Dua Lipa": ["dua lipa"],
    "Ceza": ["ceza", "ceza rap"],
    "Sagopa Kajmer": ["sagopa", "sagopa kajmer", "kajmer"],
    "Ferdi Tayfur": ["ferdi tayfur", "ferdi"],
    "Neset Ertas": ["neset ertas"],
    "Muzeyyen Senar": ["muzeyyen senar", "senar"],
    "Kazim Koyuncu": ["kazim koyuncu", "koyuncu"],
    "Zeki Muren": ["zeki muren"],
    "Gripin": ["gripin"],
    "Teoman": ["teoman"],
    "Pinhani": ["pinhani"],
    "Seksendort": ["seksendort", "80 dort"],
    "Cem Karaca": ["cem karaca"],
    "Selda Bagcan": ["selda bagcan", "selda"],
    "Limp Bizkit": ["limp bizkit"],
    "Rage Against the Machine": ["rage against", "ratm"],
    "David Guetta": ["david guetta", "guetta"],
    "Bad Bunny": ["bad bunny"],
    "John Denver": ["john denver"],
    "Deva Premal": ["deva premal"],
    "Deuter": ["deuter"],
    "Nina Simone": ["nina simone"],
    "Dean Martin": ["dean martin"],
    "Mariah Carey": ["mariah carey"],
    "Calvin Harris": ["calvin harris"],
    "Against The Current": ["against the current"],
    "Bee Gees": ["bee gees"],
    "Stevie Wonder": ["stevie wonder"],
    "Nujabes": ["nujabes"],
    "B.B. King": ["bb king"],
    "Robert Johnson": ["robert johnson"],
    "Johnny Cash": ["johnny cash"],
    "The Doors": ["the doors", "jim morrison"],
    "Pharrell Williams": ["pharrell", "pharrell williams"],
    "Miley Cyrus": ["miley", "miley cyrus"],
    "Childish Gambino": ["childish gambino", "donald glover"],
}


CATEGORY_LIST = [
    {"label": "Genel Türler", "section": True},
    {"label": "Rock", "message": "Bana rock müzik öner", "icon": "🎸"},
    {"label": "Pop", "message": "Pop şarkılar öner", "icon": "🎵"},
    {"label": "Rap / Hip-Hop", "message": "Rap müzik öner", "icon": "🎤"},
    {"label": "Jazz", "message": "Jazz müzik öner", "icon": "🎷"},
    {"label": "Klasik", "message": "Klasik müzik öner", "icon": "🎻"},
    {"label": "Lo-fi", "message": "Lo-fi müzik öner", "icon": "🎧"},
    {"label": "Elektronik", "message": "Elektronik müzik öner", "icon": "🎹"},
    {"label": "R&B / Soul", "message": "R&B ve soul öner", "icon": "🎤"},
    {"label": "Metal", "message": "Metal müzik öner", "icon": "🤘"},
    {"label": "Indie", "message": "Indie müzik öner", "icon": "🎯"},
    {"label": "Funk / Disco", "message": "Funk ve disco öner", "icon": "🕺"},
    {"label": "Blues", "message": "Blues müzik öner", "icon": "🎺"},
    {"label": "Türkçe Türler", "section": True},
    {"label": "Türkçe Pop", "message": "Türkçe pop şarkılar öner", "icon": "🇹🇷"},
    {"label": "Anadolu Rock", "message": "Anadolu rock öner", "icon": "🎸"},
    {"label": "Arabesk", "message": "Arabesk şarkılar öner", "icon": "🎭"},
    {"label": "Türkçe Rap", "message": "Türkçe rap öner", "icon": "🎤"},
    {"label": "Halk Müziği", "message": "Türk halk müziği öner", "icon": "🪕"},
    {"label": "Damar", "message": "Damar şarkılar öner", "icon": "💔"},
    {"label": "Ruh Hali", "section": True},
    {"label": "Mutlu", "message": "Mutlu edici müzik öner", "icon": "😊"},
    {"label": "Üzgün", "message": "Üzgün müzik öner", "icon": "😢"},
    {"label": "Romantik", "message": "Romantik müzik öner", "icon": "❤️"},
    {"label": "Enerjik", "message": "Enerjik müzik öner", "icon": "⚡"},
    {"label": "Sakin", "message": "Sakin müzik öner", "icon": "🌿"},
    {"label": "Motivasyon", "message": "Motivasyon şarkıları öner", "icon": "💪"},
    {"label": "Nostaljik", "message": "Nostaljik şarkılar öner", "icon": "🌅"},
    {"label": "Ortam / Aktivite", "section": True},
    {"label": "Ders Çalışma", "message": "Ders çalışırken dinleyeceğim müzik öner", "icon": "📚"},
    {"label": "Spor / Gym", "message": "Spor yaparken dinleyeceğim müzik öner", "icon": "🏃"},
    {"label": "Gece Yolculuğu", "message": "Gece yolculuğunda dinleyeceğim müzik öner", "icon": "🌙"},
    {"label": "Uyku", "message": "Uyumadan önce dinleyeceğim müzik öner", "icon": "😴"},
    {"label": "Parti", "message": "Parti müziği öner", "icon": "🎉"},
    {"label": "Yağmurlu Hava", "message": "Yağmurlu havada dinlenecek müzik öner", "icon": "🌧️"},
    {"label": "Araba Sürüşü", "message": "Arabada dinleyeceğim müzik öner", "icon": "🚗"},
    {"label": "Oyun / Gaming", "message": "Oyun oynarken dinleyeceğim müzik öner", "icon": "🎮"},
    {"label": "Kod Yazma", "message": "Kod yazarken dinleyeceğim müzik öner", "icon": "💻"},
    {"label": "Odaklanma", "message": "Odaklanmam gereken müzik öner", "icon": "🧠"},
    {"label": "Meditasyon", "message": "Meditasyon için müzik öner", "icon": "🧘"},
    {"label": "Kahve Modu", "message": "Kahve eşliğinde müzik öner", "icon": "☕"},
]


class MessageAnalyzer:
    MIN_SUBSTRING_LEN = 4

    def __init__(self):
        self.genre_keywords = GENRE_KEYWORDS
        self.mood_keywords = MOOD_KEYWORDS
        self.activity_keywords = ACTIVITY_KEYWORDS
        self.artist_keywords = ARTIST_KEYWORDS
        self.playlist_keywords = [
            "playlist", "liste", "listesi", "karisik", "karma",
            "olustur", "yap", "hazirla", "ver", "oneri", "tavsiye",
            "sarki oner", "parca oner", "muzik oner",
            "dinleyeyim", "dinlemelik", "sarkilar", "parcalar",
            "set", "mix",
        ]

    def _normalize(self, text):
        text = text.lower().strip()
        for tr_char, en_char in TURKISH_REPLACEMENTS.items():
            text = text.replace(tr_char, en_char)
        return text

    def _fuzzy_match(self, text, keywords, strict=False, allow_short_substr=False):
        text_norm = self._normalize(text)
        text_words = set(re.findall(r'[a-z0-9]+', text_norm))
        matches = []
        for category, words in keywords.items():
            for word in words:
                word_norm = self._normalize(word)
                word_parts = word_norm.split()
                if len(word_parts) > 1:
                    if word_norm in text_norm:
                        matches.append((category, len(word_norm)))
                else:
                    use_strict = strict or (len(word_norm) < self.MIN_SUBSTRING_LEN and not allow_short_substr)
                    if use_strict:
                        if word_norm in text_words:
                            matches.append((category, len(word_norm)))
                    else:
                        if word_norm in text_norm:
                            matches.append((category, len(word_norm)))
        if not matches:
            return None
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[0][0]

    def _fuzzy_match_all(self, text, keywords, strict=False, allow_short_substr=False):
        text_norm = self._normalize(text)
        text_words = set(re.findall(r'[a-z0-9]+', text_norm))
        category_best = {}
        for category, words in keywords.items():
            for word in words:
                word_norm = self._normalize(word)
                word_parts = word_norm.split()
                if len(word_parts) > 1:
                    if word_norm in text_norm:
                        prev = category_best.get(category, 0)
                        if len(word_norm) > prev:
                            category_best[category] = len(word_norm)
                else:
                    use_strict = strict or (len(word_norm) < self.MIN_SUBSTRING_LEN and not allow_short_substr)
                    found = False
                    if use_strict:
                        found = word_norm in text_words
                    else:
                        found = word_norm in text_norm
                    if found:
                        prev = category_best.get(category, 0)
                        if len(word_norm) > prev:
                            category_best[category] = len(word_norm)
        sorted_cats = sorted(category_best.items(), key=lambda x: x[1], reverse=True)
        return [cat for cat, _ in sorted_cats]

    def analyze(self, message):
        result = {
            "genre": None,
            "genres": [],
            "mood": None,
            "activity": None,
            "artist": None,
            "language": None,
            "is_playlist_request": False,
            "playlist_count": 10,
            "confidence": 0.0,
            "keywords": [],
        }

        text = message.strip()
        text_lower = text.lower()
        text_norm = self._normalize(text)

        is_karisik = "karisik" in text_norm or "karma" in text_norm or "mixed" in text_lower

        result["is_playlist_request"] = self._detect_playlist_request(text_lower)

        if not result["is_playlist_request"]:
            count_match = re.search(r"(\d+)\s*(sarki|parca|tur|sanatci|sarkilik)", text_norm)
            if count_match:
                result["is_playlist_request"] = True
                result["playlist_count"] = min(int(count_match.group(1)), 30)

        if is_karisik:
            result["language"] = "mixed"
            result["keywords"].append("dil:karisik")
            result["confidence"] += 0.1

        genres_found = self._fuzzy_match_all(text, self.genre_keywords, strict=True)
        if genres_found:
            result["genre"] = genres_found[0]
            result["genres"] = genres_found
            for g in genres_found:
                result["keywords"].append(f"tur:{g}")
            result["confidence"] += 0.3

        mood = self._fuzzy_match(text, self.mood_keywords, strict=False, allow_short_substr=True)
        if mood:
            result["mood"] = mood
            result["keywords"].append(f"ruh hali:{mood}")
            result["confidence"] += 0.3

        activity = self._fuzzy_match(text, self.activity_keywords, strict=False)
        if activity:
            result["activity"] = activity
            result["keywords"].append(f"aktivite:{activity}")
            result["confidence"] += 0.25

        artist = self._fuzzy_match(text, self.artist_keywords, strict=True)
        if artist:
            result["artist"] = artist
            result["keywords"].append(f"sanatci:{artist}")
            result["confidence"] += 0.4

        if not is_karisik:
            if "turkce" in text_norm or "yerli" in text_norm:
                result["language"] = "tr"
                result["keywords"].append("dil:turkce")
            elif "yabanci" in text_norm or "ingilizce" in text_norm or "english" in text_norm:
                result["language"] = "en"
                result["keywords"].append("dil:yabanci")
        elif "karisik" in text_norm or "karma" in text_norm:
            result["language"] = "mixed"
            result["keywords"].append("dil:karisik")

        result["confidence"] = min(result["confidence"], 1.0)

        if result["confidence"] == 0:
            result["confidence"] = self._guess_from_context(text_norm)

        return result

    def _detect_playlist_request(self, text_lower):
        strict_indicators = [
            "playlist", "liste yap", "listesi", "liste olustur", "liste ver",
            "karisik liste", "karma liste", "karisik playlist",
            "sarki listesi", "muzik listesi",
            "sarkilik liste", "parca listesi",
        ]
        count_pattern = r"(\d+)\s*(sarki|parca|tur|sanatci)\s*(liste|listesi|playlist|karisik|karma)"
        if any(ind in text_lower for ind in strict_indicators):
            return True
        if re.search(count_pattern, text_lower):
            return True
        return False

    def _guess_from_context(self, text_norm):
        filler_words = ["muzik", "sarki", "dinle", "bisey", "birsey", "onere", "tavsiye", "iste"]
        if any(w in text_norm for w in filler_words):
            return 0.15
        return 0.05


class ResponseGenerator:
    GREETINGS = ["merhaba", "selam", "hey", "naber", "nasilsin", "gunaydin", "iyi aksamlar", "iyi gunler", "hi", "hello"]
    THANKS = ["tesekkür", "tesekkur", "sagol", "eyvallah", "tşk", "tsk", "sag ol", "thanks", "thank"]
    GREETING_BLOCKERS = ["muzik", "sarki", "oner", "dinle", "playlist", "liste", "tur", "rock", "pop", "rap", "jazz", "klasik"]

    CORRECTION_PHRASES = [
        "degil", "olmadi", "yanlis", "olmuyor", "olmadı", "değil",
        "istemem", "istemedim", "bosa", "beko", "cikti", "çıkış",
        "bosa gitti", "bosh", "kotu", "kötü", "berbat", "hicbiri", "hic biri",
        "eslesmiyor", "uymuyor", "tutmadı", "tutmiyor", "bekledigim degil",
    ]
    GENRE_CORRECTION_PHRASES = [
        "hip hop", "hiphop", "rap degil", "rock degil", "pop degil",
        "rap değil", "rock değil", "pop değil", "jazz değil",
        "turkce olsun", "yabanci olsun", "türkçe olsun", "yabancı olsun",
    ]
    REJECTION_PHRASES = [
        "olmadi", "olmadı", "istemem", "begenmedim", "beğenmedim",
        "baska", "başka", "farkli", "farklı", "degistir", "değiştir",
        "olmuyor", "cikmadi", "çıkma",
    ]
    CONTINUE_PHRASES = [
        "iyiyim", "tamam", "olur", "dogru", "evet", "super", "harika",
        "guzei", "güzel", "begendim", "beğendim", "tesekkür", "tesekkur",
        "devam", "daha", "baska oner", "başka öner", "farkli oner", "farklı öner",
    ]
    MORE_PHRASES = [
        "daha", "baska", "başka", "farkli", "farklı", "biraz daha",
        "daha fazla", "baska oner", "başka öner", "devam", "daha oner", "daha öner",
    ]
    MOOD_CHANGE_PHRASES = [
        "aslj", "artjk", "sinirliyim", "mutluyum", "uzgunum", "enerjik",
        "sakinim", "yorgunum", "bitti", "degistim", "değiştim",
    ]

    MOOD_ACKNOWLEDGE_AND_ASK_ACTIVITY = {
        "mutlu": [
            "İyi hissediyorsun, harika! Peki şu an ne yapıyorsun? Spor mu, ders mi, yoksa yolculuk mu? Ona göre önerelim. 😊",
            "Mutlusun, süper! Ama söyle — ne yapıyorsun? Evde mi, dışarıda mı, spor mu, dinlenme mi? Ona göre önerelim.",
            "Keyifli bir anındasın galiba! Ne yapıyorsun şu an? Ona göre müzik seçelim.",
        ],
        "uzgun": [
            "Üzgün hissediyorsun... Peki şu an ne yapıyorsun? Bazen müzik iyi gelir, ama türü önemli — evde mi, yolda mı?",
            "Seni anlıyorum. Ne yapıyorsun şu an? Ona göre bir şeyler çıkaralım ki tam isabet olsun.",
            "Öyle günler oluyor... Ne yapıyorsun şimdi? Dinlenme modunda mısın, yoksa hareket mi ediyorsun?",
        ],
        "enerjik": [
            "Enerjin dorukta! Peki bu enerjiyi neye harcıyorsun? Spor mu, parti mi, yoksa arabada mı? Ona göre ritim seçelim.",
            "Harika bir enerji! Ne yapıyorsun şu an? Her duruma göre başka bir müzik var.",
            "Dinamik hissediyorsun! Bu enerjiyle ne yapıyorsun? Ona göre bir playlist çıkartalım.",
        ],
        "sakin": [
            "Sakinsin, iyi. Peki ne yapıyorsun şu an? Kitap mı, kahve mi, yoksa yatma vakti mi? Ona göre seçelim.",
            "Rahat bir an... Ne yapıyorsun? Meditasyon mu, dinlenme mi? Ona göre müzik bulalım.",
        ],
        "romantik": [
            "Romantik bir an... Peki ne yapıyorsun? Akşam yemeği mi, sakin bir akşam mı? Ona göre müzik seçelim.",
            "Aşk havada! Ne yapıyorsun şu an? Bir sürpriz mi planlıyorsun? Ona göre çıkaralım.",
        ],
        "asik": [
            "Aşık mısın! Peki ne yapıyorsun şu an? Yürüyüşte misin, hayal mi kuruyorsun? Ona göre şarkılar seçelim.",
            "Aşk güzel bir şey! Ama söyle bakalım — ne yapıyorsun? Ona göre müzik seçelim.",
        ],
        "motivasyon": [
            "Güç toplama zamanı! Ama ne için? Spor mu, ders mi, iş mi? Ona göre sana gaz verecek müzikler bulalım.",
            "Motivasyon mu lazım? Söyle bakalım — ne yapıyorsun? Ona göre doğru müziği seçelim.",
        ],
        "sinirli": [
            "Sinirlisin galiba... Peki ne yapıyorsun? Spor yaparak stres atmak mı istersin, yoksa sakinleşecek bir şeyler mi?",
            "Gergin bir an... Ne yapıyorsun? Stres atmak için sert bir şeyler mi, yatıştıracak bir şeyler mi ararsın?",
        ],
        "melankolik": [
            "Melankolik hissediyorsun... Peki ne yapıyorsun? Yalnız mı oturuyorsun, yolda mısın? Ona göre çıkaralım.",
            "Duygusal bir an... Ne yapıyorsun şu an? Ona göre seni anlayan müzikler bulalım.",
        ],
        "nostaljik": [
            "Nostaljik bir an... Peki ne yapıyorsun? Eski fotoğuflara mı bakıyorsun, arabada mı? Ona göre şarkılar seçelim.",
            "Geçmişe yolculuk! Ne yapıyorsun şu an? Ona göre müzik seçelim.",
        ],
        "guclu": [
            "Güçlü hissediyorsun! Bu enerjiyle ne yapıyorsun? Spor mu, bir şey mi başarmaya çalışıyorsun? Ona göre seçelim.",
            "Sert bir enerji! Ne yapıyorsun şu an? Ona göre ritim bulalım.",
        ],
        "epik": [
            "Epik bir his! Peki ne yapıyorsun? Bir şeye mi hazırlanıyorsun? Ona göre müzik seçelim.",
            "Devasa hisler! Ne yapıyorsun şu an? Ona göre büyüleyici bir şeyler bulalım.",
        ],
    }

    ACTIVITY_RECOMMEND_MESSAGES = {
        "ders": [
            "O zaman dikkatini dağıtmayacak sakin bir şey iyi gider. İşte birkaç öneri:",
            "Ders çalışırken odaklanmaya yardım edecek müzikler buldum:",
        ],
        "spor": [
            "Spor yaparken enerji dolu müzikler şart! İşte ritim tutturacak parçalar:",
            "Gym modu! Harekete geçirecek parçalar geliyor:",
        ],
        "gece": [
            "Gece vakti için atmosferik müzikler işte:",
            "Geceye uygun, atmosferik parçalar buldum:",
        ],
        "yolculuk": [
            "Yolculuk şarkıları! Uzayıp giden yollara eşlik edecek parçalar:",
            "Yolda giderken dinlenecek müzikler işte:",
        ],
        "uyku": [
            "Uyumadan önce sakinleşmeye yardım edecek müzikler:",
            "Rahatlamana ve uykuya geçmene yardım edecek parçalar:",
        ],
        "parti": [
            "Parti modu! Harekete geçirecek ritimler:",
            "Dans ettirecek parçalar geliyor:",
        ],
        "kahve": [
            "Kahve yanında müzik — en güzel kombinasyon! İşte öneriler:",
            "Kahve moduna uygun rahat parçalar:",
        ],
        "yagmur": [
            "Yağmurlu havanın en iyi müzik arkadaşı — işte öneriler:",
            "Yağmur eşliğinde dinlenecek parçalar:",
        ],
        "araba": [
            "Araba sürüşü için en iyi müzik — yolun ritmini tutturacak parçalar:",
            "Yol müziği! İşte araba için öneriler:",
        ],
        "kosu": [
            "Koşarken ritmi tutturacak parçalar:",
            "Koşu için enerji dolu müzikler:",
        ],
        "oyun": [
            "Gaming modu! Adrenalin garantili parçalar:",
            "Oyun oynarken tempo tutacak müzikler:",
        ],
        "kod": [
            "Kod yazarken odaklanmaya yardım edecek müzikler:",
            "Programcı modu! Rahat odaklanacağın parçalar:",
        ],
        "chill": [
            "Chill modu! Rahatlatan parçalar geliyor:",
            "Rahat bir an için rahat bir müzik — işte öneriler:",
        ],
        "odak": [
            "Odaklanmak için sakin ama motive eden müzikler:",
            "Derin odak için parçalar buldum:",
        ],
        "meditasyon": [
            "Meditasyon için huzur verici müzikler:",
            "Zihinsel rahatlama için sakin ve derin parçalar:",
        ],
    }

    ASK_MOOD_MESSAGES = [
        "Merhaba! 😄 Bugün nasılsın?",
        "Hey, hoş geldin! Bugün nasıl hissediyorsun?",
        "Selamlar! Ruh halin nasıl bugün? Ona göre bir şeyler çıkaralım.",
        "Merhaba! Bugün nasıl bir gününde olduğun anlat bakalım, ona göre müzik önereyim.",
    ]

    ASK_ACTIVITY_MESSAGES = {
        "mutlu": [
            "Anladım, iyi hissediyorsun! Peki şu an ne yapıyorsun? Ders mi çalışıyorsun, spor mu, yoksa sadece dinlenme modunda mısın?",
            "Mutlusun, harika! Peki ne yapıyorsun şu an? Ona göre müzik seçelim.",
        ],
        "uzgun": [
            "Anladım, yorucu bir gün olmuş gibi. Peki şu an ne yapıyorsun? Evde mi oturuyorsun, yoksa bir yerde mi?",
            "Seni anlıyorum. Peki ne yapıyorsun şu an? Dinlenme modunda mısın, yoksa bir şeyler mi yapıyorsun?",
        ],
        "enerjik": [
            "Enerjin dorukta! Peki bu enerjiyle ne yapıyorsun? Spor mu, dans mı, yoksa yolda mı?",
            "Harika bir enerji! Ne yapıyorsun? Ona göre ritim seçelim.",
        ],
        "sakin": [
            "Sakin bir an... Peki ne yapıyorsun? Kitap mı, kahve mi, meditasyon mu?",
            "Rahat moddasın. Ne yapıyorsun şu an? Ona göre müzik seçelim.",
        ],
        "romantik": ["Romantik bir an... Peki ne yapıyorsun? Akşam yemeği mi, sakin bir akşam mı?"],
        "asik": ["Aşık mısın! Peki ne yapıyorsun şu an? Ona göre şarkılar seçelim."],
        "motivasyon": ["Güç toplama zamanı! Peki ne için? Spor mu, ders mi, iş mi?"],
        "sinirli": [
            "Gergin bir gün... Peki ne yapıyorsun? Stres atmak için spor mu, yoksa sakinleşmek mi istersin?",
            "Sinirlisin galiba. Peki ne yapıyorsun şu an? Sert bir şeyler mi, sakinleştirici mi ararsın?",
        ],
        "melankolik": ["Melankolik bir an... Peki ne yapıyorsun? Yalnız mı, yolda mı?"],
        "nostaljik": ["Nostaljik hissediyorsun. Peki ne yapıyorsun şu an? Ona göre geçmişe götürecek şarkılar seçelim."],
        "guclu": ["Güçlü hissediyorsun! Bu enerjiyle ne yapıyorsun?"],
        "epik": ["Epik bir his! Peki ne yapıyorsun? Ona göre büyüleyici müzikler seçelim."],
    }

    GENERIC_ASK_ACTIVITY = [
        "Peki şu an ne yapıyorsun? Ders mi, spor mu, yolculuk mu, yoksa sadece dinlenme modunda mısın?",
        "Ne yapıyorsun şu an? Ona göre daha isabetli bir şey önerebilirim.",
        "Peki neyle meşgulün şu an? Ona göre müzik seçelim.",
    ]

    def __init__(self, songs_db=None):
        self.songs_db = songs_db or DEMO_SONGS

    def generate_response(self, user_message, analysis, user_prefs=None, stage="asking_mood", session_context=None):
        import random as _rnd
        session_context = session_context or {}

        stored_mood = session_context.get("mood")
        stored_genre = session_context.get("genre")
        stored_genres = session_context.get("genres") or []
        stored_activity = session_context.get("activity")
        stored_artist = session_context.get("artist")
        stored_language = session_context.get("language")

        new_mood = analysis.get("mood")
        new_genre = analysis.get("genre")
        new_genres = analysis.get("genres") or []
        new_activity = analysis.get("activity")
        new_artist = analysis.get("artist")
        new_language = analysis.get("language")

        current_mood = new_mood or stored_mood
        current_genre = new_genre or stored_genre
        current_genres = new_genres if new_genres else stored_genres
        current_activity = new_activity or stored_activity
        current_artist = new_artist or stored_artist
        current_language = new_language or stored_language

        if stage == "asking_activity" and stored_mood and new_mood and new_mood != stored_mood:
            current_mood = stored_mood

        new_context = {
            "mood": current_mood,
            "genre": current_genre,
            "genres": current_genres,
            "activity": current_activity,
            "artist": current_artist,
            "language": current_language,
        }

        msg_lower = user_message.lower().strip()
        from_normalize = self._normalize_static(msg_lower)

        is_greeting = self._is_greeting(msg_lower, from_normalize)
        is_thanks = self._is_thanks(msg_lower, from_normalize)

        if is_thanks:
            thanks_replies = [
                "Rica ederim! Başka bir şey istersen buradayım.",
                "Ne demek, her zaman. Yeni bir şeyler keşfetmek istersen söyle.",
                "Beğenmene sevindim! Daha fazla öneri mi istersin?",
            ]
            return {
                "message": _rnd.choice(thanks_replies),
                "songs": [],
                "ask_more": True,
                "stage": stage,
                "context": new_context,
            }

        if is_greeting:
            return {
                "message": _rnd.choice(self.ASK_MOOD_MESSAGES),
                "songs": [],
                "ask_more": True,
                "stage": "asking_mood",
                "context": new_context,
            }

        has_direct_request = bool(current_genre or current_artist)

        is_correction = self._is_correction(msg_lower, from_normalize)
        is_genre_change = self._is_genre_correction(user_message, analysis, session_context)
        is_rejection = self._is_rejection(msg_lower, from_normalize)
        is_continue = self._is_continue(msg_lower, from_normalize)
        is_more = self._is_more(msg_lower, from_normalize)

        if stage == "recommending":
            if is_genre_change:
                correction_genre = new_genre or analysis.get("genre")
                correction_language = new_language or analysis.get("language")
                if correction_genre:
                    current_genre = correction_genre
                    current_genres = new_genres if new_genres else [correction_genre]
                if correction_language:
                    current_language = correction_language

                songs = self._select_songs(current_genre, current_mood, current_activity, current_artist, current_language, count=3, extra_genres=current_genres)

                genre_label = GENRE_LABELS.get(current_genre, current_genre) if current_genre else ""
                genre_lang_note = ""
                if current_language:
                    genre_lang_note = f" ({'Türkçe' if current_language == 'tr' else 'Yabancı'})"
                mood_note = ""
                if current_mood:
                    mood_note = f" {MOOD_LABELS.get(current_mood, current_mood)} ruh halini koruyarak"
                act_note = ""
                if current_activity:
                    act_note = f" {ACTIVITY_LABELS.get(current_activity, current_activity)} ortamına uygun"

                message = f"Haklısın, düzeltiyorum{mood_note}{act_note}— bu kez {genre_label}{genre_lang_note} ağırlıklı öneriler:\n\n"
                if songs:
                    song_lines = []
                    for i, s in enumerate(songs, 1):
                        line = f"**{s['name']}** — {s['artist']}"
                        sm = s.get("mood", "")
                        if sm:
                            line += f" *({sm})*"
                        song_lines.append(f"{i}. {line}")
                    message += "\n".join(song_lines)
                message += "\n\nDaha fazla öneri ister misin? Tür, ruh hali değiştirebilirsin."

                new_context = {"mood": current_mood, "genre": current_genre, "genres": current_genres, "activity": current_activity, "artist": current_artist, "language": current_language}
                return {"message": message, "songs": songs, "ask_more": True, "stage": "recommending", "context": new_context}

            if is_correction or is_rejection:
                songs = self._select_songs(current_genre, current_mood, current_activity, current_artist, current_language, count=3, extra_genres=current_genres)

                mood_note = ""
                if current_mood:
                    mood_note = f" {MOOD_LABELS.get(current_mood, current_mood)} ruh haline ve"
                act_note = ""
                if current_activity:
                    act_note = f" {ACTIVITY_LABELS.get(current_activity, current_activity)} ortamına uygun"
                genre_note = ""
                if current_genre:
                    genre_note = f" {GENRE_LABELS.get(current_genre, current_genre)}"

                corr_replies = [
                    "Anlıyorum, o zaman senin istediğin tarafa gidelim!",
                    "Haklısın, düzeltiyorum!",
                    "Tamam, bu kez daha isabetli olmaya çalışayım!",
                ]
                import random as _rnd_c
                message = _rnd_c.choice(corr_replies) + f"\n\n{mood_note}{genre_note}{act_note} yeni öneriler:\n\n"
                if songs:
                    song_lines = []
                    for i, s in enumerate(songs, 1):
                        line = f"**{s['name']}** — {s['artist']}"
                        sm = s.get("mood", "")
                        if sm:
                            line += f" *({sm})*"
                        song_lines.append(f"{i}. {line}")
                    message += "\n".join(song_lines)
                message += "\n\nDaha fazla öneri ister misin? Tür, ruh hali değiştirebilirsin."

                return {"message": message, "songs": songs, "ask_more": True, "stage": "recommending", "context": new_context}

            if is_more:
                songs = self._select_songs(current_genre, current_mood, current_activity, current_artist, current_language, count=3, extra_genres=current_genres)
                message = self._build_recommendation_message(current_mood, current_activity, current_genre, current_artist, songs, user_prefs)
                return {"message": message, "songs": songs, "ask_more": True, "stage": "recommending", "context": new_context}

            if is_continue and not new_mood and not new_activity and not new_genre and not new_artist:
                cont_replies = [
                    "Harika! Başka bir şey ister misin? Tür, ruh hali veya aktivite değiştirebilirsin.",
                    "Beğenmene sevindim! Daha fazla öneri ister misin?",
                    "Süper! Başka bir tür veya ruh hali de denemek ister misin?",
                ]
                import random as _rnd_cr
                return {"message": _rnd_cr.choice(cont_replies), "songs": [], "ask_more": True, "stage": "recommending", "context": new_context}

        if stage == "asking_mood":
            if current_mood and current_activity:
                songs = self._select_songs(current_genre, current_mood, current_activity, current_artist, current_language, count=3, extra_genres=current_genres)
                message = self._build_recommendation_message(current_mood, current_activity, current_genre, current_artist, songs, user_prefs)
                return {
                    "message": message,
                    "songs": songs,
                    "ask_more": True,
                    "stage": "recommending",
                    "context": new_context,
                }
            elif current_mood:
                message = self._acknowledge_mood_ask_activity(current_mood)
                return {
                    "message": message,
                    "songs": [],
                    "ask_more": True,
                    "stage": "asking_activity",
                    "context": new_context,
                }
            elif has_direct_request:
                songs = self._select_songs(current_genre, None, None, current_artist, current_language, count=3, extra_genres=current_genres)
                message = self._build_direct_with_question(current_genre, current_artist, songs, question="mood")
                return {
                    "message": message,
                    "songs": songs,
                    "ask_more": True,
                    "stage": "asking_mood",
                    "context": new_context,
                }
            else:
                reask = [
                    "Nasıl hissediyorsun şu an? Mutlu mu, üzgün mü, enerjik mi? Anlat bakalım, ona göre müzik seçelim. 😊",
                    "Ruh halini anlatırsan daha iyi öneri yapabilirim! Nasıl hissediyorsun?",
                    "Önce ruh halini anlat — sonra müzik seçelim. Nasıl hissediyorsun bugün?",
                ]
                return {
                    "message": _rnd.choice(reask),
                    "songs": [],
                    "ask_more": True,
                    "stage": "asking_mood",
                    "context": new_context,
                }

        elif stage == "asking_activity":
            if current_activity:
                songs = self._select_songs(current_genre, current_mood, current_activity, current_artist, current_language, count=3, extra_genres=current_genres)
                message = self._build_recommendation_message(current_mood, current_activity, current_genre, current_artist, songs, user_prefs)
                return {
                    "message": message,
                    "songs": songs,
                    "ask_more": True,
                    "stage": "recommending",
                    "context": new_context,
                }
            elif has_direct_request:
                songs = self._select_songs(current_genre, current_mood, None, current_artist, current_language, count=3, extra_genres=current_genres)
                message = self._build_direct_with_question(current_genre, current_artist, songs, question="activity")
                return {
                    "message": message,
                    "songs": songs,
                    "ask_more": True,
                    "stage": "recommending",
                    "context": new_context,
                }
            elif current_mood and not current_activity:
                mood_changed = analysis.get("mood") and session_context.get("mood") and analysis.get("mood") != session_context.get("mood")
                if mood_changed:
                    new_context["activity"] = None
                    message = self._acknowledge_mood_ask_activity(current_mood)
                    return {
                        "message": message,
                        "songs": [],
                        "ask_more": True,
                        "stage": "asking_activity",
                        "context": new_context,
                    }
                reask_act = [
                    "Peki şu an ne yapıyorsun? Ders mi çalışıyorsun, spor mu, yoksa sadece dinlenme modunda mısın?",
                    "Neyle meşgulün şu an? Bir aktivite söylersen daha isabetli öneri yapabilirim.",
                    "Şu an ne yapıyorsun? Yolda mı, evde mi, ders mi, spor mu? Ona göre seçelim.",
                ]
                return {
                    "message": _rnd.choice(reask_act),
                    "songs": [],
                    "ask_more": True,
                    "stage": "asking_activity",
                    "context": new_context,
                }
            else:
                reask = [
                    "Ne yapıyorsun şu an? Bir aktivite söylersen daha isabetli müzik önerebilirim.",
                    "Şu an neyle meşgulsün? Ders, spor, yolculuk, dinlenme... Hangisi?",
                ]
                return {
                    "message": _rnd.choice(reask),
                    "songs": [],
                    "ask_more": True,
                    "stage": "asking_activity",
                    "context": new_context,
                }

        return {
            "message": _rnd.choice(self.ASK_MOOD_MESSAGES),
            "songs": [],
            "ask_more": True,
            "stage": "asking_mood",
            "context": new_context,
        }

    @staticmethod
    def _normalize_static(text):
        result = text.lower().strip()
        for tr_char, en_char in TURKISH_REPLACEMENTS.items():
            result = result.replace(tr_char, en_char)
        return result

    @staticmethod
    def _is_greeting(msg_lower, msg_norm):
        greetings = ["merhaba", "selam", "hey", "naber", "nasilsin", "gunaydin", "iyi aksamlar", "iyi gunler", "hi", "hello"]
        blockers = ["muzik", "sarki", "oner", "dinle", "playlist", "liste", "tur", "rock", "pop", "rap", "jazz", "klasik", "metal", "lofi", "blues", "indie"]
        return any(g in msg_norm for g in greetings) and not any(w in msg_norm for w in blockers)

    @staticmethod
    def _is_thanks(msg_lower, msg_norm):
        thanks = ["tesekkür", "tesekkur", "sagol", "eyvallah", "sag ol", "thanks", "thank"]
        return any(t in msg_norm for t in thanks)

    @staticmethod
    def _is_correction(msg_lower, msg_norm):
        phrases = [
            "degil", "olmadi", "yanlis", "olmuyor", "olmadı", "değil",
            "istemem", "istemedim", "bosa", "kotu", "kötü", "berbat",
            "hicbiri", "hic biri", "eslesmiyor", "uymuyor", "tutmiyor",
            "bekledigim degil", "olmuyor", "olmadı",
        ]
        return any(p in msg_norm for p in phrases)

    def _is_genre_correction(self, user_message, analysis, session_context):
        new_genre = analysis.get("genre")
        new_genres = analysis.get("genres") or []
        new_language = analysis.get("language")
        old_genre = session_context.get("genre") if session_context else None
        old_genres = session_context.get("genres") or [] if session_context else []
        if new_genre and old_genre and new_genre != old_genre:
            return True
        if new_genre and not old_genre and (new_genres or new_language):
            return True
        msg_norm = self._normalize_static(user_message.lower())
        genre_change_phrases = [
            "rap olsun", "rock olsun", "pop olsun", "jazz olsun",
            "klasik olsun", "metal olsun", "lofi olsun", "blues olsun",
            "turkce olsun", "türkçe olsun", "yabanci olsun", "yabancı olsun",
            "degil", "değil", "olsun",
        ]
        has_genre_word = bool(new_genre or new_genres)
        has_change_word = any(p in msg_norm for p in ["olsun", "degil", "değil"])
        has_not = any(p in msg_norm for p in ["degil", "değil"])
        if has_genre_word and has_change_word:
            return True
        if has_not and has_genre_word:
            return True
        return False

    @staticmethod
    def _is_rejection(msg_lower, msg_norm):
        phrases = [
            "istemem", "begenmedim", "beğenmedim", "olmadi", "olmadı",
            "baska", "başka", "farkli", "farklı", "degistir", "değiştir",
            "olmuyor", "cikmadi",
        ]
        return any(p in msg_norm for p in phrases)

    @staticmethod
    def _is_continue(msg_lower, msg_norm):
        phrases = [
            "iyiyim", "tamam", "olur", "dogru", "evet", "super",
            "harika", "guzel", "güzel", "begendim", "beğendim",
        ]
        return any(p in msg_norm for p in phrases)

    @staticmethod
    def _is_more(msg_lower, msg_norm):
        phrases = [
            "daha", "baska", "başka", "farkli", "farklı", "biraz daha",
            "daha fazla", "devam", "daha oner", "daha öner",
        ]
        has_more = any(p in msg_norm for p in phrases)
        has_not_reject = not any(p in msg_norm for p in ["degil", "değil", "istemem", "olmadi", "olmadı", "yanlis"])
        return has_more and has_not_reject

    def _acknowledge_mood_ask_activity(self, mood):
        import random as _rnd
        options = self.MOOD_ACKNOWLEDGE_AND_ASK_ACTIVITY.get(mood, self.GENERIC_ASK_ACTIVITY)
        return _rnd.choice(options)

    def _build_recommendation_message(self, mood, activity, genre, artist, songs, user_prefs=None, extra_genres=None):
        import random as _rnd
        parts = []
        genre_label = GENRE_LABELS.get(genre, genre) if genre else None

        if mood and activity:
            mood_label = MOOD_LABELS.get(mood, mood) if mood else mood
            activity_label = ACTIVITY_LABELS.get(activity, activity) if activity else activity
            openers = [
                f"{mood_label} ruh hali ve {activity_label} durumu için sana birkaç öneri:",
                f"{mood_label} hissedip {activity_label} yapıyorsun — tam sana göre parçalar:",
                f"Anladım! {mood_label} + {activity_label} kombinasyonu için önerilerim:",
            ]
            parts.append(_rnd.choice(openers))
        elif mood:
            mood_label = MOOD_LABELS.get(mood, mood) if mood else mood
            mood_rec = {
                "mutlu": "Keyifli bir anındasın — sana uygun parçalar:",
                "uzgun": "Üzgün hissettiğini duyup da sessiz kalamam. Gerçekten empati yapabildiğim parçalar:",
                "enerjik": "Enerjin dorukta! Bu ritimler tam sana göre:",
                "romantik": "Romantik havaya uygun parçalar:",
                "asik": "Aşık birine yüreğini titretecek parçalar:",
                "sakin": "Sakinlesmek için harika bir seçim — işte öneriler:",
                "motivasyon": "Güç toplama zamanı! Sana gaz verecek parçalar:",
                "sinirli": "Öfke ve stresten kurtulmana yardım edecek parçalar:",
                "melankolik": "Melankolik anların yolidaşı olacak parçalar:",
                "nostaljik": "Geçmişe götürecek, nostaljik parçalar:",
                "guclu": "Güçlü hissetmen için sert ve güçlü ritimler:",
                "epik": "Epik ve büyüleyici parçalar:",
            }
            parts.append(mood_rec.get(mood, f"{mood_label} ruh haline uygun parçalar:"))
        elif activity:
            activity_label = ACTIVITY_LABELS.get(activity, activity) if activity else activity
            act_msgs = self.ACTIVITY_RECOMMEND_MESSAGES.get(activity, [f"{activity_label} için öneriler:"])
            parts.append(_rnd.choice(act_msgs))
        elif genre_label:
            parts.append(f"{genre_label} türünde birkaç öneri:")
        elif artist:
            parts.append(f"{artist} sevenler için birkaç öneri:")

        if not parts:
            parts.append("Sana birkaç öneri:")

        if songs:
            song_lines = []
            for i, s in enumerate(songs, 1):
                line = f"**{s['name']}** — {s['artist']}"
                song_mood = s.get("mood", "")
                if song_mood:
                    line += f" *({song_mood})*"
                song_lines.append(f"{i}. {line}")
            parts.append("\n\n" + "\n".join(song_lines))

        follow_ups = [
            "Başka bir şey de istersen söyle!",
            "Nasıl, beğendin mi? Başka tür veya ruh hali de önerabilirim.",
            "Daha fazla öneri ister misin? Tür, ruh hali değiştirebilirsin.",
        ]
        parts.append("\n\n" + _rnd.choice(follow_ups))

        if user_prefs and user_prefs.get("liked_genres"):
            liked = ", ".join(user_prefs["liked_genres"][:2])
            parts.append(f"\n\n💡 Arada {liked} sevdiğini hatırlıyorum, belki bu da hoşuna gider!")

        return " ".join(parts)

    def _select_songs(self, genre=None, mood=None, activity=None, artist=None, language=None, count=3, extra_genres=None):
        import random
        target_genres = list(extra_genres) if extra_genres else ([genre] if genre else [])
        candidates = list(self.songs_db)
        scored = []
        for song in candidates:
            score = 0
            song_genres = song.get("genres", [])
            if target_genres:
                genre_overlap = set(song_genres) & set(target_genres)
                if genre_overlap:
                    score += len(genre_overlap) * 3
            if mood and mood in song.get("moods", []):
                score += 2
            if activity and activity in song.get("activities", []):
                score += 2
            if artist and song.get("artist", "").lower() == artist.lower():
                score += 5
            if language:
                if language == "tr" and song.get("language") == "tr":
                    score += 1
                elif language == "en" and song.get("language") == "en":
                    score += 1
                elif language == "mixed":
                    score += 0.5
            scored.append((score, song))

        scored.sort(key=lambda x: x[0], reverse=True)

        if target_genres:
            high_score = [s for sc, s in scored if any(g in s.get("genres", []) for g in target_genres)]
            low_score = [s for sc, s in scored if not any(g in s.get("genres", []) for g in target_genres)]
            random.shuffle(high_score)
            random.shuffle(low_score)
            unique = []
            seen = set()
            for s in high_score + low_score:
                key = f"{s['name']}_{s['artist']}"
                if key not in seen:
                    seen.add(key)
                    unique.append(s)
            if len(unique) < count:
                remaining = [s for s in self.songs_db if f"{s['name']}_{s['artist']}" not in seen]
                random.shuffle(remaining)
                unique.extend(remaining)
            return [self._song_to_dict(s) for s in unique[:count]]

        top = [s for sc, s in scored if sc > 0][:count]
        if len(top) < count:
            remaining = [s for sc, s in scored if sc == 0]
            random.shuffle(remaining)
            top.extend(remaining[: count - len(top)])
        return [self._song_to_dict(s) for s in top[:count]]

    def _song_to_dict(self, s):
        genres = s.get("genres", [])
        return {
            "name": s.get("name", ""),
            "artist": s.get("artist", ""),
            "album": s.get("album", ""),
            "genre": genres[0] if genres else "",
            "genres": genres,
            "genre_label": GENRE_LABELS.get(genres[0], "") if genres else "",
            "mood": s.get("moods", [""])[0] if s.get("moods") else "",
            "language": s.get("language", ""),
            "cover_url": s.get("cover_url", ""),
            "spotify_url": s.get("spotify_url", ""),
            "reason": s.get("reason", ""),
            "duration": s.get("duration", ""),
        }

    def _build_direct_with_question(self, genre, artist, songs, question="mood"):
        import random as _rnd
        parts = []
        genre_label = GENRE_LABELS.get(genre, genre) if genre else None
        if genre_label:
            parts.append(f"{genre_label} turunde bir kac oneri buldum!")
        elif artist:
            parts.append(f"{artist} sevenler icin bir kac oneri buldum!")
        else:
            parts.append("Iste bir kac oneri:")
        if songs:
            song_lines = []
            for i, s in enumerate(songs, 1):
                line = f"**{s['name']}** — {s['artist']}"
                song_lines.append(f"{i}. {line}")
            parts.append("\n\n" + "\n".join(song_lines))
        if question == "mood":
            parts.append("\n\nPeki şu an nasıl hissediyorsun? Ona göre daha isabetli öneri yapabilirim.")
        elif question == "activity":
            parts.append("\n\nPeki şu an ne yapıyorsun? Ona göre daha iyi eşleştirebilirim.")
        return " ".join(parts)