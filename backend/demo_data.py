GENRE_LABELS = {
    "rock": "Rock",
    "pop": "Pop",
    "rap": "Rap / Hip-Hop",
    "trap": "Trap",
    "rnb": "R&B / Soul",
    "jazz": "Jazz",
    "blues": "Blues",
    "klasik": "Klasik Müzik",
    "metal": "Metal",
    "punk": "Punk",
    "indie": "Indie",
    "alternatif_rock": "Alternatif Rock",
    "elektronik": "Elektronik",
    "edm": "EDM",
    "house": "House",
    "techno": "Techno",
    "lofi": "Lo-fi",
    "ambient": "Ambient",
    "reggaeton": "Reggaeton",
    "country": "Country",
    "folk": "Folk",
    "soul": "Soul",
    "funk": "Funk",
    "disko": "Disco",
    "turkce_pop": "Türkçe Pop",
    "turkce_rap": "Türkçe Rap",
    "arabesk": "Arabesk",
    "thm": "Türk Halk Müziği",
    "tsm": "Türk Sanat Müziği",
    "anadolu_rock": "Anadolu Rock",
    "fantazi": "Fantazi",
    "damar": "Damar",
    "karadeniz": "Karadeniz",
    "oyun_havasi": "Oyun Havası",
    "synthpop": "Synth-Pop",
    "grunge": "Grunge",
    "neoklasik": "Neoklasik",
    "psychedelik": "Psychedelik",
    "hiphop": "Hip-Hop",
}

MOOD_LABELS = {
    "mutlu": "Mutlu",
    "uzgun": "Üzgün",
    "asik": "Aşık",
    "enerjik": "Enerjik",
    "sakin": "Sakin",
    "motivasyon": "Motivasyon",
    "sinirli": "Sinirli",
    "melankolik": "Melankolik",
    "nostaljik": "Nostaljik",
    "romantik": "Romantik",
}

ACTIVITY_LABELS = {
    "ders": "Ders Çalışma",
    "spor": "Spor / Gym",
    "gece": "Gece Yolculuğu",
    "parti": "Parti",
    "kahve": "Kahve Modu",
    "yagmur": "Yağmurlu Hava",
    "yazlik": "Yazlık",
    "kislik": "Kışlık",
    "sabah": "Sabah Dinleme",
    "uyku": "Uyku Öncesi",
    "kosu": "Koşu",
    "araba": "Araba Sürüşü",
    "oyun": "Oyun Oynama",
    "kod": "Kod Yazma",
    "yayin": "Yayın Açarken",
    "chill": "Chill",
    "odak": "Odaklanma",
    "meditasyon": "Meditasyon",
}

CATEGORY_LIST = [
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
    {"label": "Türkçe Pop", "message": "Türkçe pop şarkılar öner", "icon": "🇹🇷"},
    {"label": "Anadolu Rock", "message": "Anadolu rock öner", "icon": "🎸"},
    {"label": "Arabesk", "message": "Arabesk şarkılar öner", "icon": "🎭"},
    {"label": "Türkçe Rap", "message": "Türkçe rap öner", "icon": "🎤"},
    {"label": "Halk Müziği", "message": "Türk halk müziği öner", "icon": "🪕"},
    {"label": "Damar", "message": "Damar şarkılar öner", "icon": "💔"},
    {"label": "Playlist Yap", "message": "Bana 10 şarkılık playlist yap", "icon": "📋"},
    {"label": "Motivasyon", "message": "Motivasyona ihtiyacım var", "icon": "💪"},
    {"label": "Üzgünüm", "message": "Moralim bozuk, ne dinleyebilirim?", "icon": "😢"},
    {"label": "Romantik", "message": "Aşk şarkısı öner", "icon": "❤️"},
    {"label": "Spor / Gym", "message": "Spor yaparken dinleyeceğim şarkılar öner", "icon": "🏃"},
    {"label": "Gece Yolculuğu", "message": "Gece yolculuğunda dinleyeceğim müzik öner", "icon": "🌙"},
    {"label": "Sakinleş", "message": "Sakinleşmek istiyorum", "icon": "🧘"},
    {"label": "Kahve Modu", "message": "Kahve eşliğinde müzik öner", "icon": "☕"},
    {"label": "Yağmurlu Hava", "message": "Yağmurlu havada dinlenecek müzik", "icon": "🌧️"},
    {"label": "Oyun Müziği", "message": "Oyun oynarken dinleyeceğim müzik öner", "icon": "🎮"},
    {"label": "Kod Yazma", "message": "Kod yazarken dinleyeceğim müzik öner", "icon": "💻"},
    {"label": "Odaklanma", "message": "Odaklanmam gereken müzik öner", "icon": "🧠"},
]

DEMO_SONGS = [
    # ========================
    # ROCK
    # ========================
    {"id": "s1", "name": "Bohemian Rhapsody", "artist": "Queen", "album": "A Night at the Opera", "genres": ["rock"], "moods": ["epik", "nostaljik", "enerjik"], "activities": ["gece", "parti"], "language": "en", "year": 1975, "duration": "5:55", "bpm": 72, "cover_url": "", "spotify_url": "https://open.spotify.com/track/4u7EnebtmKWfsU3Q5OB0vY", "reason": "Rock muziginin efsanevi eseri"},
    {"id": "s2", "name": "Hotel California", "artist": "Eagles", "album": "Hotel California", "genres": ["rock"], "moods": ["nostaljik", "sakin"], "activities": ["gece", "araba", "yagmur"], "language": "en", "year": 1977, "duration": "6:30", "bpm": 75, "cover_url": "", "spotify_url": "https://open.spotify.com/track/40riOy7x9W7GXjyGp4pjAv", "reason": "Klasik rock twisti"},
    {"id": "s3", "name": "Stairway to Heaven", "artist": "Led Zeppelin", "album": "Led Zeppelin IV", "genres": ["rock"], "moods": ["nostaljik", "sakin", "melankolik"], "activities": ["gece", "yagmur"], "language": "en", "year": 1971, "duration": "8:02", "bpm": 82, "cover_url": "", "spotify_url": "https://open.spotify.com/track/5CQ30WqJwcep0pYcV4AMNw", "reason": "Rock tarihinin en buyuk eseri"},
    {"id": "s4", "name": "Smells Like Teen Spirit", "artist": "Nirvana", "album": "Nevermind", "genres": ["rock", "grunge"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "parti"], "language": "en", "year": 1991, "duration": "5:01", "bpm": 117, "cover_url": "", "spotify_url": "https://open.spotify.com/track/5ghIJDpPoe3CfHMGu71E6T", "reason": "Grunge rockin sembol eseri"},
    {"id": "s5", "name": "Enter Sandman", "artist": "Metallica", "album": "Metallica", "genres": ["metal", "rock"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "kosu"], "language": "en", "year": 1991, "duration": "5:31", "bpm": 123, "cover_url": "", "spotify_url": "https://open.spotify.com/track/2P3EOqsv3qIVF4r8tqlDIR", "reason": "Metalin efsane eseri"},
    {"id": "s6", "name": "Back in Black", "artist": "AC/DC", "album": "Back in Black", "genres": ["rock"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "parti"], "language": "en", "year": 1980, "duration": "4:15", "bpm": 125, "cover_url": "", "spotify_url": "https://open.spotify.com/track/08mG3Y1vljYA6BVq5TqtCP", "reason": "Enerjik rock klasiği"},
    {"id": "s7", "name": "Yesterday", "artist": "The Beatles", "album": "Help!", "genres": ["rock", "pop"], "moods": ["uzgun", "nostaljik", "melankolik"], "activities": ["gece", "yagmur"], "language": "en", "year": 1965, "duration": "2:05", "bpm": 96, "cover_url": "", "spotify_url": "https://open.spotify.com/track/3JBEXC2mQtOY5gW0JwkjA4", "reason": "Muzik tarihinin en coverlanan sarkisi"},
    {"id": "s8", "name": "Comfortably Numb", "artist": "Pink Floyd", "album": "The Wall", "genres": ["rock"], "moods": ["sakin", "melankolik"], "activities": ["gece", "ders", "yagmur"], "language": "en", "year": 1979, "duration": "6:23", "bpm": 64, "cover_url": "", "spotify_url": "https://open.spotify.com/track/2sAwMRW1YfMMS7CM0pIPVQ", "reason": "Progressive rockin zirvesi"},
    {"id": "s9", "name": "We Will Rock You", "artist": "Queen", "album": "News of the World", "genres": ["rock"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "parti"], "language": "en", "year": 1977, "duration": "2:01", "bpm": 134, "cover_url": "", "spotify_url": "#none", "reason": "Stadyum rock klasiği"},
    {"id": "s10", "name": "Over The Hills and Far Away", "artist": "Led Zeppelin", "album": "Houses of the Holy", "genres": ["rock"], "moods": ["mutlu", "enerjik"], "activities": ["araba", "yazlik"], "language": "en", "year": 1973, "duration": "3:47", "bpm": 116, "cover_url": "", "spotify_url": "#none", "reason": "Led Zeppelin'in klasik eseri"},

    # ========================
    # POP
    # ========================
    {"id": "s11", "name": "Rolling in the Deep", "artist": "Adele", "album": "21", "genres": ["pop", "soul"], "moods": ["uzgun", "enerjik", "asik"], "activities": ["gece"], "language": "en", "year": 2010, "duration": "3:48", "bpm": 105, "cover_url": "", "spotify_url": "https://open.spotify.com/track/1s8hPfJJqAIYCBCAFKcsx5", "reason": "Guclu vokaliyle unlu"},
    {"id": "s12", "name": "Shape of You", "artist": "Ed Sheeran", "album": "Divide", "genres": ["pop"], "moods": ["mutlu", "romantik"], "activities": ["parti", "araba"], "language": "en", "year": 2017, "duration": "3:53", "bpm": 96, "cover_url": "", "spotify_url": "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3", "reason": "Pop muzigin en populer sarkilarindan"},
    {"id": "s13", "name": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours", "genres": ["pop", "synthpop"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "araba", "gece"], "language": "en", "year": 2019, "duration": "3:20", "bpm": 171, "cover_url": "", "spotify_url": "https://open.spotify.com/track/0VjIjWZGlKPV3gqS2TSt4e", "reason": "80'ler sentezi modern pop"},
    {"id": "s14", "name": "Levitating", "artist": "Dua Lipa", "album": "Future Nostalgia", "genres": ["pop", "disko"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "spor"], "language": "en", "year": 2020, "duration": "3:23", "bpm": 103, "cover_url": "", "spotify_url": "https://open.spotify.com/track/463CkQjx2Zk1r1nS8sJeT1", "reason": "Eglenceli disko pop"},
    {"id": "s15", "name": "Someone Like You", "artist": "Adele", "album": "21", "genres": ["pop", "soul"], "moods": ["uzgun", "romantik", "nostaljik"], "activities": ["gece", "yagmur"], "language": "en", "year": 2011, "duration": "4:45", "bpm": 68, "cover_url": "", "spotify_url": "https://open.spotify.com/track/1zwMYTA3R7Ms7EN3NS3qoP", "reason": "Duygusal pop baladi"},
    {"id": "s16", "name": "Watermelon Sugar", "artist": "Harry Styles", "album": "Fine Line", "genres": ["pop", "funk"], "moods": ["mutlu", "romantik"], "activities": ["parti", "yazlik"], "language": "en", "year": 2019, "duration": "2:54", "bpm": 95, "cover_url": "", "spotify_url": "https://open.spotify.com/track/6Jb8WK50cNjPqbba8V7WFX", "reason": "Yaz ruhlari pop sarkisi"},
    {"id": "s17", "name": "Thinking Out Loud", "artist": "Ed Sheeran", "album": "x", "genres": ["pop", "soul"], "moods": ["romantik", "sakin"], "activities": ["kahve"], "language": "en", "year": 2014, "duration": "4:41", "bpm": 79, "cover_url": "", "spotify_url": "#none", "reason": "Romantik popun klasiği"},

    # ========================
    # RAP / HIP-HOP
    # ========================
    {"id": "s20", "name": "Lose Yourself", "artist": "Eminem", "album": "8 Mile OST", "genres": ["rap"], "moods": ["motivasyon", "enerjik"], "activities": ["spor", "kosu", "gym"], "language": "en", "year": 2002, "duration": "5:26", "bpm": 171, "cover_url": "", "spotify_url": "https://open.spotify.com/track/5Z01UMMf7i1R1hsJ4N2kWr", "reason": "Motivasyon sarkilarinin krali"},
    {"id": "s21", "name": "HUMBLE.", "artist": "Kendrick Lamar", "album": "DAMN.", "genres": ["rap", "hiphop"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "parti"], "language": "en", "year": 2017, "duration": "2:57", "bpm": 150, "cover_url": "", "spotify_url": "https://open.spotify.com/track/7KXjTSCq3n2fmoR3x9MLDq", "reason": "Modern rapin guclu eseri"},
    {"id": "s22", "name": "God's Plan", "artist": "Drake", "album": "Scorpion", "genres": ["rap", "hiphop"], "moods": ["mutlu", "motivasyon"], "activities": ["parti", "araba"], "language": "en", "year": 2018, "duration": "3:18", "bpm": 77, "cover_url": "", "spotify_url": "https://open.spotify.com/track/6DCZcSspforMqJYH9hjFMH", "reason": "Drake'in imza sarkisi"},
    {"id": "s23", "name": "Sicko Mode", "artist": "Travis Scott", "album": "Astroworld", "genres": ["rap", "trap"], "moods": ["enerjik", "sinirli"], "activities": ["parti", "oyun"], "language": "en", "year": 2018, "duration": "5:12", "bpm": 155, "cover_url": "", "spotify_url": "https://open.spotify.com/track/2xYWxM8sGZRkE5PcWO8RkF", "reason": "Yaratici trap prodiksiyonu"},
    {"id": "s24", "name": "Can't Hold Us", "artist": "Macklemore & Ryan Lewis", "album": "The Heist", "genres": ["rap", "pop"], "moods": ["enerjik", "mutlu", "motivasyon"], "activities": ["spor", "parti", "kosu"], "language": "en", "year": 2012, "duration": "4:18", "bpm": 146, "cover_url": "", "spotify_url": "#none", "reason": "Enerjik rap-pop karisimi"},
    {"id": "s25", "name": "Stronger", "artist": "Kanye West", "album": "Graduation", "genres": ["rap", "elektronik"], "moods": ["motivasyon", "enerjik"], "activities": ["spor", "gym"], "language": "en", "year": 2007, "duration": "5:11", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Guc veren rap klasiği"},

    # ========================
    # JAZZ
    # ========================
    {"id": "s30", "name": "So What", "artist": "Miles Davis", "album": "Kind of Blue", "genres": ["jazz"], "moods": ["sakin", "nostaljik"], "activities": ["gece", "ders", "kahve"], "language": "en", "year": 1959, "duration": "9:22", "bpm": 134, "cover_url": "", "spotify_url": "https://open.spotify.com/track/7i5mSzmmqrOBuDsjDGhM0G", "reason": "Jazz muziginin basyapidi"},
    {"id": "s31", "name": "Take Five", "artist": "Dave Brubeck", "album": "Time Out", "genres": ["jazz"], "moods": ["sakin", "motivasyon"], "activities": ["ders", "gece", "kahve"], "language": "en", "year": 1959, "duration": "5:24", "bpm": 180, "cover_url": "", "spotify_url": "https://open.spotify.com/track/1p8UYQ4R6v6JAtO9vJh7RJ", "reason": "5/4 olcumu ile efsane jazz"},
    {"id": "s32", "name": "What a Wonderful World", "artist": "Louis Armstrong", "album": "What a Wonderful World", "genres": ["jazz"], "moods": ["mutlu", "romantik", "sakin"], "activities": ["sabah", "kahve"], "language": "en", "year": 1967, "duration": "2:21", "bpm": 72, "cover_url": "", "spotify_url": "https://open.spotify.com/track/4R63ftqz7MD7HRsBadSAUR", "reason": "Dunyanin en guzel sarkilarndan"},

    # ========================
    # KLASIK
    # ========================
    {"id": "s35", "name": "Clair de Lune", "artist": "Claude Debussy", "album": "Suite bergamasque", "genres": ["klasik"], "moods": ["sakin", "romantik", "melankolik"], "activities": ["uyku", "ders", "gece", "yagmur"], "language": "en", "year": 1905, "duration": "5:12", "bpm": 54, "cover_url": "", "spotify_url": "https://open.spotify.com/track/2cr1MBxPr1fQM3lJC7TSJm", "reason": "Piyano klasiklerinin en guzeli"},
    {"id": "s36", "name": "Fur Elise", "artist": "Ludwig van Beethoven", "album": "Bagatelles", "genres": ["klasik"], "moods": ["sakin", "romantik"], "activities": ["ders", "uyku"], "language": "en", "year": 1810, "duration": "3:00", "bpm": 80, "cover_url": "", "spotify_url": "https://open.spotify.com/track/2J6J8Y6Z38U0h3lit3hrdT", "reason": "Piyano klasikleri baslangici"},
    {"id": "s37", "name": "The Four Seasons - Spring", "artist": "Antonio Vivaldi", "album": "The Four Seasons", "genres": ["klasik"], "moods": ["mutlu", "enerjik"], "activities": ["sabah", "ders"], "language": "en", "year": 1725, "duration": "3:30", "bpm": 140, "cover_url": "", "spotify_url": "https://open.spotify.com/track/5Iy3Gtd9s3hTncsdYspy4G", "reason": "Baharin muziksel resmi"},
    {"id": "s38", "name": "River Flows in You", "artist": "Yiruma", "album": "First Love", "genres": ["klasik", "neoklasik"], "moods": ["romantik", "sakin", "melankolik"], "activities": ["uyku", "ders", "yagmur"], "language": "en", "year": 2001, "duration": "3:12", "bpm": 67, "cover_url": "", "spotify_url": "#none", "reason": "Romantik piyano muafiyeti"},

    # ========================
    # METAL
    # ========================
    {"id": "s40", "name": "Fear of the Dark", "artist": "Iron Maiden", "album": "Fear of the Dark", "genres": ["metal"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "en", "year": 1992, "duration": "7:11", "bpm": 168, "cover_url": "", "spotify_url": "#none", "reason": "Heavy metal efsanesi"},
    {"id": "s41", "name": "Paranoid", "artist": "Black Sabbath", "album": "Paranoid", "genres": ["metal"], "moods": ["enerjik", "sinirli"], "activities": ["spor"], "language": "en", "year": 1970, "duration": "2:48", "bpm": 140, "cover_url": "", "spotify_url": "#none", "reason": "Metal muzigin temel tasi"},
    {"id": "s42", "name": "Master of Puppets", "artist": "Metallica", "album": "Master of Puppets", "genres": ["metal", "thrash"], "moods": ["enerjik", "sinirli", "motivasyon"], "activities": ["spor", "gym", "oyun"], "language": "en", "year": 1986, "duration": "8:35", "bpm": 212, "cover_url": "", "spotify_url": "#none", "reason": "Thrash metalin zirvesi"},

    # ========================
    # PUNK
    # ========================
    {"id": "s45", "name": "Blitzkrieg Bop", "artist": "Ramones", "album": "Ramones", "genres": ["punk"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "parti"], "language": "en", "year": 1976, "duration": "2:12", "bpm": 167, "cover_url": "", "spotify_url": "#none", "reason": "Punk rockin heyecan verici baslangici"},
    {"id": "s46", "name": "Holiday", "artist": "Green Day", "album": "American Idiot", "genres": ["punk", "alternatif_rock"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "araba"], "language": "en", "year": 2004, "duration": "3:52", "bpm": 170, "cover_url": "", "spotify_url": "#none", "reason": "Punk pop klasiği"},

    # ========================
    # INDIE / ALTERNATIF
    # ========================
    {"id": "s50", "name": "Do I Wanna Know?", "artist": "Arctic Monkeys", "album": "AM", "genres": ["indie", "alternatif_rock"], "moods": ["melankolik", "enerjik"], "activities": ["gece", "araba"], "language": "en", "year": 2013, "duration": "4:32", "bpm": 85, "cover_url": "", "spotify_url": "#none", "reason": "Indie rockin modern klasiği"},
    {"id": "s51", "name": "The Less I Know the Better", "artist": "Tame Impala", "album": "Currents", "genres": ["indie", "psychedelik"], "moods": ["mutlu", "romantik"], "activities": ["araba", "yazlik"], "language": "en", "year": 2015, "duration": "3:36", "bpm": 116, "cover_url": "", "spotify_url": "#none", "reason": "Psychedelik pop klasiği"},
    {"id": "s52", "name": "Someday", "artist": "The Strokes", "album": "Is This It", "genres": ["indie", "alternatif_rock"], "moods": ["nostaljik", "enerjik"], "activities": ["araba", "yazlik"], "language": "en", "year": 2001, "duration": "3:05", "bpm": 106, "cover_url": "", "spotify_url": "#none", "reason": "Garaj rockin en iyisi"},
    {"id": "s53", "name": "Sunday Candy", "artist": "Donnie Trumpet", "album": "Surf", "genres": ["indie", "soul"], "moods": ["mutlu", "sakin"], "activities": ["sabah", "kahve"], "language": "en", "year": 2015, "duration": "4:15", "bpm": 110, "cover_url": "", "spotify_url": "#none", "reason": "Sevimli indie-soul sarkisi"},

    # ========================
    # BLUES
    # ========================
    {"id": "s55", "name": "The Thrill Is Gone", "artist": "B.B. King", "album": "Completely Well", "genres": ["blues"], "moods": ["uzgun", "sakin"], "activities": ["gece", "yagmur", "kahve"], "language": "en", "year": 1969, "duration": "5:23", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": "Blues'un en taninmis eseri"},
    {"id": "s56", "name": "Cross Road Blues", "artist": "Robert Johnson", "album": "King of the Delta Blues", "genres": ["blues"], "moods": ["uzgun", "melankolik"], "activities": ["gece"], "language": "en", "year": 1936, "duration": "2:47", "bpm": 108, "cover_url": "", "spotify_url": "#none", "reason": "Delta bluesun babasi"},

    # ========================
    # ELEKTRONIK / EDM / HOUSE / TECHNO
    # ========================
    {"id": "s60", "name": "Get Lucky", "artist": "Daft Punk", "album": "Random Access Memories", "genres": ["elektronik", "funk"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba", "yazlik"], "language": "en", "year": 2013, "duration": "4:08", "bpm": 116, "cover_url": "", "spotify_url": "#none", "reason": "Funk ve elektronik muhtesem bilesimi"},
    {"id": "s61", "name": "Wake Me Up", "artist": "Avicii", "album": "True", "genres": ["elektronik", "edm"], "moods": ["enerjik", "mutlu", "motivasyon"], "activities": ["spor", "parti", "kosu"], "language": "en", "year": 2013, "duration": "4:07", "bpm": 124, "cover_url": "", "spotify_url": "#none", "reason": "Avicii'nin unutulmaz eseri"},
    {"id": "s62", "name": "Levels", "artist": "Avicii", "album": "True", "genres": ["elektronik", "edm"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "spor"], "language": "en", "year": 2011, "duration": "3:18", "bpm": 126, "cover_url": "", "spotify_url": "#none", "reason": "EDM klasiği"},
    {"id": "s63", "name": "Strobe", "artist": "Deadmau5", "album": "For Lack of a Better Name", "genres": ["elektronik", "house"], "moods": ["sakin", "melankolik"], "activities": ["gece", "araba", "chill"], "language": "en", "year": 2009, "duration": "10:37", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "Progressive housun basyapidi"},
    {"id": "s64", "name": "Midnight City", "artist": "M83", "album": "Hurry Up, We're Dreaming", "genres": ["elektronik", "synthpop"], "moods": ["nostaljik", "sakin"], "activities": ["gece", "araba"], "language": "en", "year": 2011, "duration": "4:03", "bpm": 105, "cover_url": "", "spotify_url": "#none", "reason": "Synth-pop gece klasiği"},
    {"id": "s65", "name": "钛 (Titanium)", "artist": "David Guetta ft. Sia", "album": "Nothing but the Beat", "genres": ["edm", "elektronik"], "moods": ["motivasyon", "enerjik"], "activities": ["spor", "parti", "gym"], "language": "en", "year": 2011, "duration": "4:05", "bpm": 126, "cover_url": "", "spotify_url": "#none", "reason": "EDM muhtesem vokal eseri"},
    {"id": "s66", "name": "One More Time", "artist": "Daft Punk", "album": "Discovery", "genres": ["house", "disko"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "yazlik"], "language": "en", "year": 2000, "duration": "5:20", "bpm": 123, "cover_url": "", "spotify_url": "#none", "reason": "House muzik klasiği"},

    # ========================
    # LO-FI / AMBIENT
    # ========================
    {"id": "s70", "name": "Aruarian Dance", "artist": "Nujabes", "album": "Metaphorical Music", "genres": ["lofi", "hiphop"], "moods": ["sakin", "nostaljik"], "activities": ["ders", "uyku", "odak", "kod"], "language": "en", "year": 2003, "duration": "4:18", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Lo-fi hip hop klasiği"},
    {"id": "s71", "name": "Sunday Morning", "artist": "Idealism", "album": "Sunday Morning", "genres": ["lofi"], "moods": ["sakin", "mutlu"], "activities": ["ders", "uyku", "kahve", "sabah"], "language": "en", "year": 2017, "duration": "2:30", "bpm": 75, "cover_url": "", "spotify_url": "#none", "reason": "Rahatlatan lo-fi sarki"},
    {"id": "s72", "name": "Weightless", "artist": "Marconi Union", "album": "Weightless", "genres": ["ambient"], "moods": ["sakin"], "activities": ["uyku", "meditasyon", "yagmur"], "language": "en", "year": 2011, "duration": "8:09", "bpm": 60, "cover_url": "", "spotify_url": "#none", "reason": "Bilimsel olarak en rahatlatici sarki"},
    {"id": "s73", "name": "Breathe", "artist": "Kupla", "album": "Breathe", "genres": ["lofi"], "moods": ["sakin", "uzgun"], "activities": ["ders", "uyku", "odak", "kod"], "language": "en", "year": 2018, "duration": "2:45", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Dinlendiran lo-fi melodi"},

    # ========================
    # R&B / SOUL / FUNK / DISCO
    # ========================
    {"id": "s75", "name": "All of Me", "artist": "John Legend", "album": "Love in the Future", "genres": ["rnb", "soul"], "moods": ["romantik", "sakin"], "activities": ["gece", "kahve"], "language": "en", "year": 2013, "duration": "4:29", "bpm": 63, "cover_url": "", "spotify_url": "#none", "reason": "Ask sarkisi klasiği"},
    {"id": "s76", "name": "Redbone", "artist": "Childish Gambino", "album": "Awaken, My Love!", "genres": ["rnb", "funk"], "moods": ["sakin", "mutlu"], "activities": ["gece", "kahve", "chill"], "language": "en", "year": 2016, "duration": "5:26", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Funk R&B bilesimi"},
    {"id": "s77", "name": "Stayin' Alive", "artist": "Bee Gees", "album": "Saturday Night Fever", "genres": ["disko", "funk"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "araba"], "language": "en", "year": 1977, "duration": "4:44", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Disko klasiği"},
    {"id": "s78", "name": "Superstition", "artist": "Stevie Wonder", "album": "Talking Book", "genres": ["funk", "soul"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "sabah"], "language": "en", "year": 1972, "duration": "4:26", "bpm": 102, "cover_url": "", "spotify_url": "#none", "reason": "Funk ve soul birlesimi"},
    {"id": "s79", "name": "Starboy", "artist": "The Weeknd", "album": "Starboy", "genres": ["rnb", "pop"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "araba"], "language": "en", "year": 2016, "duration": "3:50", "bpm": 192, "cover_url": "", "spotify_url": "#none", "reason": "Modern R&B pop"},

    # ========================
    # COUNTRY / FOLK / REGGAETON
    # ========================
    {"id": "s82", "name": "Take Me Home, Country Roads", "artist": "John Denver", "album": "Poems, Prayers & Promises", "genres": ["country", "folk"], "moods": ["nostaljik", "mutlu"], "activities": ["araba", "yazlik"], "language": "en", "year": 1971, "duration": "3:10", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Country folk klasiği"},
    {"id": "s83", "name": "Ho Hey", "artist": "The Lumineers", "album": "The Lumineers", "genres": ["folk", "indie"], "moods": ["mutlu", "romantik"], "activities": ["araba", "kahve"], "language": "en", "year": 2012, "duration": "2:42", "bpm": 138, "cover_url": "", "spotify_url": "#none", "reason": "Folk pop sevilen eser"},
    {"id": "s84", "name": "Dakiti", "artist": "Bad Bunny & Jhay Cortez", "album": "El Ultimo Tour Del Mundo", "genres": ["reggaeton"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "gym"], "language": "es", "year": 2020, "duration": "3:27", "bpm": 114, "cover_url": "", "spotify_url": "#none", "reason": "Reggaeton global hit"},

    # ========================
    # TURKCE POP
    # ========================
    {"id": "s100", "name": "Simarik", "artist": "Tarkan", "album": "Olurum Sana", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik", "romantik"], "activities": ["parti", "araba"], "language": "tr", "year": 1997, "duration": "3:30", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Turk popunun dunyaya acilan kapisi"},
    {"id": "s101", "name": "Gideriyorum", "artist": "Sezen Aksu", "album": "Gideriyorum", "genres": ["turkce_pop"], "moods": ["uzgun", "nostaljik"], "activities": ["gece", "araba", "yagmur"], "language": "tr", "year": 1998, "duration": "4:10", "bpm": 90, "cover_url": "", "spotify_url": "#none", "reason": "Turk popunun efsane ismi"},
    {"id": "s102", "name": "Hadi Ozelim", "artist": "Kenan Dogulu", "album": "Kenan Dogulu", "genres": ["turkce_pop"], "moods": ["mutlu", "romantik"], "activities": ["parti", "yazlik"], "language": "tr", "year": 2007, "duration": "3:45", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "Eglenceli turkce pop"},
    {"id": "s103", "name": "Senden Daha Guzel", "artist": "Gulsen", "album": "Soz", "genres": ["turkce_pop"], "moods": ["mutlu", "romantik"], "activities": ["parti"], "language": "tr", "year": 2019, "duration": "3:10", "bpm": 118, "cover_url": "", "spotify_url": "#none", "reason": "Mutlu turkce pop sarkisi"},
    {"id": "s104", "name": "Yagmurla Gelen", "artist": "Sezen Aksu", "album": "Yagmurla Gelen", "genres": ["turkce_pop"], "moods": ["uzgun", "melankolik"], "activities": ["yagmur", "gece"], "language": "tr", "year": 1995, "duration": "4:05", "bpm": 80, "cover_url": "", "spotify_url": "#none", "reason": "Yagmurla gelen duygusal sarki"},

    # ========================
    # TURKCE RAP
    # ========================
    {"id": "s106", "name": "Benim Adim Frekans", "artist": "Ceza", "album": "Rapstar", "genres": ["turkce_rap"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "tr", "year": 2006, "duration": "3:50", "bpm": 95, "cover_url": "", "spotify_url": "#none", "reason": "Turkce rapin onde gelen ismi"},
    {"id": "s107", "name": "Galiba", "artist": "Sagopa Kajmer", "album": "Bir Pesimistin Gunlugu", "genres": ["turkce_rap"], "moods": ["melankolik", "uzgun"], "activities": ["gece", "yagmur"], "language": "tr", "year": 2005, "duration": "4:15", "bpm": 85, "cover_url": "", "spotify_url": "#none", "reason": "Turkce rapin duygusal yuzu"},

    # ========================
    # ARABESK / DAMAR / FANTAZI
    # ========================
    {"id": "s110", "name": "Aglama", "artist": "Muslum Gurses", "album": "Muslum Gurses", "genres": ["arabesk", "damar"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1989, "duration": "4:10", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Arabesk muzigin efsanesi"},
    {"id": "s111", "name": "Beni Yalniz Birakma", "artist": "Ibrahim Tatlises", "album": "Beni Yalniz Birakma", "genres": ["arabesk"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1992, "duration": "3:45", "bpm": 75, "cover_url": "", "spotify_url": "#none", "reason": "Arabesk romantik"},
    {"id": "s112", "name": "Cemile", "artist": "Muslum Gurses", "album": "Cemile", "genres": ["arabesk", "damar"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1985, "duration": "4:15", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Arabesk damarin en guzeli"},
    {"id": "s113", "name": "Boyle Aklima Gelmemeliydi", "artist": "Ferdi Tayfur", "album": "Boyle Aklima Gelmemeliydi", "genres": ["arabesk", "fantazi"], "moods": ["uzgun", "melankolik"], "activities": ["gece"], "language": "tr", "year": 1988, "duration": "3:50", "bpm": 73, "cover_url": "", "spotify_url": "#none", "reason": "Arabesk romantik klasiği"},

    # ========================
    # TURK HALK MUZIGI / KARADENIZ / OYUN HAVASI
    # ========================
    {"id": "s116", "name": "Uskudar'a Gider Iken", "artist": "Neset Ertas", "album": "Neset Ertas", "genres": ["thm"], "moods": ["nostaljik", "mutlu"], "activities": ["araba", "gece"], "language": "tr", "year": 1970, "duration": "3:20", "bpm": 96, "cover_url": "", "spotify_url": "#none", "reason": "Turk halk muzigi klasiği"},
    {"id": "s117", "name": "Cane Cane", "artist": "Muzeyyen Senar", "album": "Muzeyyen Senar", "genres": ["tsm", "thm"], "moods": ["nostaljik", "mutlu"], "activities": ["gece"], "language": "tr", "year": 1965, "duration": "3:40", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Turk sanat muzigi efsanesi"},
    {"id": "s118", "name": "Laz Laz", "artist": "Kazim Koyuncu", "album": "Hayde", "genres": ["karadeniz"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "araba"], "language": "tr", "year": 2001, "duration": "3:15", "bpm": 140, "cover_url": "", "spotify_url": "#none", "reason": "Karadeniz muzigin enerjisi"},
    {"id": "s119", "name": "Ankaranin Baglari", "artist": "Zeki Muren", "album": "Zeki Muren", "genres": ["tsm", "oyun_havasi"], "moods": ["mutlu", "enerjik"], "activities": ["parti"], "language": "tr", "year": 1968, "duration": "2:55", "bpm": 105, "cover_url": "", "spotify_url": "#none", "reason": "Oyun havasi klasiği"},

    # ========================
    # ANADOLU ROCK
    # ========================
    {"id": "s122", "name": "Daglar Daglar", "artist": "Baris Manco", "album": "Baris Manco", "genres": ["anadolu_rock"], "moods": ["nostaljik", "mutlu"], "activities": ["araba", "gece"], "language": "tr", "year": 1977, "duration": "4:20", "bpm": 110, "cover_url": "", "spotify_url": "#none", "reason": "Anadolu rockin efsanelerinden"},
    {"id": "s123", "name": "Islak Islak", "artist": "Duman", "album": "Belki Alismam Lazim", "genres": ["turkce_rock"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 2002, "duration": "4:33", "bpm": 96, "cover_url": "", "spotify_url": "#none", "reason": "Turkce rockin duygusal yuzu"},
    {"id": "s124", "name": "Cevapsiz Sorular", "artist": "maNga", "album": "maNga", "genres": ["turkce_rock"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "tr", "year": 2004, "duration": "3:44", "bpm": 130, "cover_url": "", "spotify_url": "#none", "reason": "Turk rock metalinin en iyisi"},
    {"id": "s125", "name": "Bir Derdim Var", "artist": "Mor ve Otesi", "album": "Dunya Yalan Soyluyor", "genres": ["turkce_rock"], "moods": ["uzgun", "sinirli"], "activities": ["gece"], "language": "tr", "year": 2004, "duration": "4:02", "bpm": 118, "cover_url": "", "spotify_url": "#none", "reason": "Alternatif turkce rock"},
    {"id": "s126", "name": "Yillar Sonra", "artist": "Sebnem Ferah", "album": "Artik Kisa Seyler Soyluyorum", "genres": ["turkce_rock"], "moods": ["nostaljik", "uzgun"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1999, "duration": "4:15", "bpm": 92, "cover_url": "", "spotify_url": "#none", "reason": "Turkce rockin kadin sesi"},
    {"id": "s127", "name": "Her Seyi Yak", "artist": "Sebnem Ferah", "album": "Artik Kisa Seyler Soyluyorum", "genres": ["turkce_rock"], "moods": ["enerjik", "motivasyon", "sinirli"], "activities": ["spor", "gym"], "language": "tr", "year": 1999, "duration": "3:55", "bpm": 140, "cover_url": "", "spotify_url": "#none", "reason": "Guclu turkce rock"},
    {"id": "s128", "name": "Benzemezsim", "artist": "Gripin", "album": "Gripin", "genres": ["turkce_rock", "pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "tr", "year": 2007, "duration": "3:30", "bpm": 125, "cover_url": "", "spotify_url": "#none", "reason": "Eglenceli turkce pop-rock"},
    {"id": "s129", "name": "Senden Baska", "artist": "Teoman", "album": "O", "genres": ["turkce_rock"], "moods": ["romantik", "uzgun"], "activities": ["gece"], "language": "tr", "year": 2000, "duration": "4:12", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Teoman'in romantik klasiği"},
    {"id": "s130", "name": "Nefes", "artist": "maNga", "album": "Sehir", "genres": ["turkce_rock"], "moods": ["uzgun", "sakin"], "activities": ["gece", "yagmur"], "language": "tr", "year": 2012, "duration": "4:05", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Duygusal turkce rock"},
    {"id": "s131", "name": "Sahilde", "artist": "Seksendort", "album": "Seksendort", "genres": ["turkce_rock", "pop"], "moods": ["mutlu", "romantik"], "activities": ["araba", "yazlik"], "language": "tr", "year": 2010, "duration": "3:15", "bpm": 115, "cover_url": "", "spotify_url": "#none", "reason": "Yaz ruhlari turkce pop-rock"},
    {"id": "s132", "name": "Elif", "artist": "Pinhani", "album": "Zor", "genres": ["turkce_rock", "indie"], "moods": ["sakin", "romantik"], "activities": ["gece", "kahve"], "language": "tr", "year": 2008, "duration": "3:45", "bpm": 72, "cover_url": "", "spotify_url": "#none", "reason": "Sakin ve romantik turkce indie"},
    {"id": "s133", "name": "Yaz Gazeteci", "artist": "Mor ve Otesi", "album": "Buyuk Dusler", "genres": ["turkce_rock"], "moods": ["nostaljik", "mutlu"], "activities": ["araba", "yazlik"], "language": "tr", "year": 1999, "duration": "3:25", "bpm": 108, "cover_url": "", "spotify_url": "#none", "reason": "Nostaljik turkce rock"},
    {"id": "s134", "name": "Gul Altin", "artist": "Cem Karaca", "album": "Cem Karaca", "genres": ["anadolu_rock"], "moods": ["nostaljik", "enerjik"], "activities": ["araba"], "language": "tr", "year": 1975, "duration": "3:45", "bpm": 105, "cover_url": "", "spotify_url": "#none", "reason": "Anadolu rockin onde gelen ismi"},
    {"id": "s135", "name": "Nem Kaldi", "artist": "Selda Bagcan", "album": "Selda", "genres": ["anadolu_rock", "folk"], "moods": ["uzgun", "sakin"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1976, "duration": "3:20", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Anadolu rock efsanesinin guclu sesi"},

    # ========================
    # MOOD-SPECIFIC ADDITIONS
    # ========================
    # MUTLU
    {"id": "s150", "name": "Happy", "artist": "Pharrell Williams", "album": "G I R L", "genres": ["pop", "funk"], "moods": ["mutlu"], "activities": ["sabah", "parti", "yazlik"], "language": "en", "year": 2013, "duration": "3:53", "bpm": 160, "cover_url": "", "spotify_url": "#none", "reason": "Mutlulugun sarkisi"},
    {"id": "s151", "name": "Walking on Sunshine", "artist": "Katrina and the Waves", "album": "Walking on Sunshine", "genres": ["pop", "rock"], "moods": ["mutlu", "enerjik"], "activities": ["sabah", "yazlik"], "language": "en", "year": 1985, "duration": "3:58", "bpm": 112, "cover_url": "", "spotify_url": "#none", "reason": "Gunesli gune muzik"},

    # ASIK
    {"id": "s155", "name": "All of Me", "artist": "John Legend", "album": "Love in the Future", "genres": ["rnb", "soul"], "moods": ["romantik", "asik"], "activities": ["gece", "kahve"], "language": "en", "year": 2013, "duration": "4:29", "bpm": 63, "cover_url": "", "spotify_url": "#none", "reason": "Ask sarkisinin klasiği"},
    {"id": "s156", "name": "Perfect", "artist": "Ed Sheeran", "album": "Divide", "genres": ["pop"], "moods": ["romantik", "asik"], "activities": ["gece", "kahve"], "language": "en", "year": 2017, "duration": "4:23", "bpm": 68, "cover_url": "", "spotify_url": "#none", "reason": "Romantik duet klasiği"},

    # SINIRLI
    {"id": "s160", "name": "Break Stuff", "artist": "Limp Bizkit", "album": "Significant Other", "genres": ["metal", "rap"], "moods": ["sinirli", "enerjik"], "activities": ["spor", "gym"], "language": "en", "year": 1999, "duration": "2:46", "bpm": 100, "cover_url": "", "spotify_url": "#none", "reason": "Ofke ve enerji bosaltma sarkisi"},
    {"id": "s161", "name": "Killing in the Name", "artist": "Rage Against the Machine", "album": "Rage Against the Machine", "genres": ["rock", "alternatif_rock"], "moods": ["sinirli", "enerjik"], "activities": ["spor", "gym"], "language": "en", "year": 1992, "duration": "5:13", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": " Asi ve enerjik rock"},

    # MELANKOLIK
    {"id": "s165", "name": "Creep", "artist": "Radiohead", "album": "Pablo Honey", "genres": ["alternatif_rock", "indie"], "moods": ["melankolik", "uzgun"], "activities": ["gece", "yagmur"], "language": "en", "year": 1993, "duration": "3:56", "bpm": 92, "cover_url": "", "spotify_url": "#none", "reason": "Melankoli klasiği"},
    {"id": "s166", "name": "Hurt", "artist": "Johnny Cash", "album": "American IV", "genres": ["country", "folk"], "moods": ["melankolik", "uzgun"], "activities": ["gece", "yagmur"], "language": "en", "year": 2002, "duration": "3:38", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Duygusal derinligiyle unlu sarki"},

    # SABAH / KAHVE
    {"id": "s170", "name": "Here Comes the Sun", "artist": "The Beatles", "album": "Abbey Road", "genres": ["rock", "pop"], "moods": ["mutlu", "sakin"], "activities": ["sabah", "kahve"], "language": "en", "year": 1969, "duration": "3:05", "bpm": 100, "cover_url": "", "spotify_url": "#none", "reason": "Sabah muzigi klasiği"},
    {"id": "s171", "name": "Feeling Good", "artist": "Nina Simone", "album": "I Put a Spell on You", "genres": ["jazz", "soul"], "moods": ["mutlu", "motivasyon"], "activities": ["sabah", "kahve"], "language": "en", "year": 1965, "duration": "2:55", "bpm": 116, "cover_url": "", "spotify_url": "#none", "reason": "Yeni gun baslangici sarkisi"},

    # OYUN
    {"id": "s175", "name": "Warriors", "artist": "Imagine Dragons", "album": "Smoke + Mirrors", "genres": ["rock"], "moods": ["enerjik", "motivasyon"], "activities": ["oyun", "spor"], "language": "en", "year": 2014, "duration": "2:50", "bpm": 140, "cover_url": "", "spotify_url": "#none", "reason": "Esport ve oyun muzigi"},
    {"id": "s176", "name": "Legends Never Die", "artist": "Against The Current", "album": "Legends Never Die", "genres": ["pop", "rock"], "moods": ["motivasyon", "enerjik"], "activities": ["oyun", "spor"], "language": "en", "year": 2017, "duration": "3:16", "bpm": 150, "cover_url": "", "spotify_url": "#none", "reason": "League of Legends klasiği"},

    # KOD YAZMA
    {"id": "s180", "name": "Still D.R.E.", "artist": "Dr. Dre ft. Snoop Dogg", "album": "2001", "genres": ["rap", "hiphop"], "moods": ["enerjik"], "activities": ["kod", "oyun"], "language": "en", "year": 1999, "duration": "4:30", "bpm": 92, "cover_url": "", "spotify_url": "#none", "reason": "Kod yazarken klasik rap"},
    {"id": "s181", "name": "Around the World", "artist": "Daft Punk", "album": "Homework", "genres": ["house", "elektronik"], "moods": ["enerjik", "sakin"], "activities": ["kod", "odak"], "language": "en", "year": 1997, "duration": "7:09", "bpm": 124, "cover_url": "", "spotify_url": "#none", "reason": "Tekrarlayan house ritmi"},

    # MEDITASYON
    {"id": "s185", "name": "Om Namah Shivaya", "artist": "Deva Premal", "album": "The Essence", "genres": ["ambient"], "moods": ["sakin"], "activities": ["meditasyon", "uyku"], "language": "en", "year": 1998, "duration": "7:30", "bpm": 60, "cover_url": "", "spotify_url": "#none", "reason": "Meditasyon muzigi klasiği"},
    {"id": "s186", "name": "Deep Peace", "artist": "Deuter", "album": "Earth Blue", "genres": ["ambient", "neoklasik"], "moods": ["sakin"], "activities": ["meditasyon", "uyku", "yagmur"], "language": "en", "year": 2003, "duration": "6:15", "bpm": 50, "cover_url": "", "spotify_url": "#none", "reason": "Derin meditasyon muzigi"},

    # YAGMURLU HAVA
    {"id": "s190", "name": "Riders on the Storm", "artist": "The Doors", "album": "L.A. Woman", "genres": ["rock"], "moods": ["melankolik", "sakin"], "activities": ["yagmur", "gece"], "language": "en", "year": 1971, "duration": "7:14", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Yagmurlu havalarin rock klasiği"},

    # KISLIK
    {"id": "s195", "name": "Let It Snow", "artist": "Dean Martin", "album": "A Winter Romance", "genres": ["pop", "jazz"], "moods": ["mutlu", "sakin"], "activities": ["kislik", "gece"], "language": "en", "year": 1966, "duration": "2:18", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": "Kis klasiği"},
    {"id": "s196", "name": "All I Want for Christmas Is You", "artist": "Mariah Carey", "album": "Merry Christmas", "genres": ["pop"], "moods": ["mutlu"], "activities": ["kislik", "parti"], "language": "en", "year": 1994, "duration": "4:01", "bpm": 127, "cover_url": "", "spotify_url": "#none", "reason": "Noel sarkisi klasiği"},

    # YAYLIK
    {"id": "s200", "name": "Summer Days", "artist": "Calvin Harris", "album": "Summer Days", "genres": ["pop", "elektronik"], "moods": ["mutlu", "enerjik"], "activities": ["yazlik", "parti", "araba"], "language": "en", "year": 2019, "duration": "3:36", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Yaz enerjisi"},

    # ========================
    # EK TURKCE SARKILAR
    # ========================
    {"id": "s201", "name": "Firari", "artist": "Sezen Aksu", "album": "Firari", "genres": ["turkce_pop"], "moods": ["uzgun", "nostaljik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 2003, "duration": "4:30", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Sezen Aksu'nun duygusal klasiği"},
    {"id": "s202", "name": "Gulduren Sehir", "artist": "Sebnem Ferah", "album": "Artik Kisa Seyler Soyluyorum", "genres": ["turkce_rock"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1999, "duration": "4:45", "bpm": 90, "cover_url": "", "spotify_url": "#none", "reason": "Sebnem Ferah'in duygusal sarkisi"},
    {"id": "s203", "name": "Araba", "artist": "Tarkan", "album": "Kara Kutu", "genres": ["turkce_pop"], "moods": ["enerjik", "mutlu"], "activities": ["araba", "parti"], "language": "tr", "year": 2002, "duration": "3:40", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "Tarkan'in eglenceli hiti"},
    {"id": "s204", "name": "Ozgurluk", "artist": "Mor ve Otesi", "album": "Buyuk Dusler", "genres": ["turkce_rock"], "moods": ["motivasyon", "enerjik"], "activities": ["spor", "araba"], "language": "tr", "year": 2006, "duration": "3:50", "bpm": 135, "cover_url": "", "spotify_url": "#none", "reason": "Guclu turkce rock"},
    {"id": "s205", "name": "Hadi Bakalim", "artist": "Kenan Dogulu", "album": "Festival", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "spor"], "language": "tr", "year": 2009, "duration": "3:20", "bpm": 125, "cover_url": "", "spotify_url": "#none", "reason": "Kenan Dogulu'nun eglenceli sarkisi"},
    {"id": "s206", "name": "Kara Toprak", "artist": "Neset Ertas", "album": "Neset Ertas", "genres": ["thm"], "moods": ["uzgun", "nostaljik"], "activities": ["gece"], "language": "tr", "year": 1970, "duration": "4:00", "bpm": 75, "cover_url": "", "spotify_url": "#none", "reason": "THM'nin efsane eseri"},
    {"id": "s207", "name": "Holvido", "artist": "Sagopa Kajmer", "album": "Bir Pesimistin Gunlugu", "genres": ["turkce_rap"], "moods": ["sinirli", "enerjik"], "activities": ["spor", "gym"], "language": "tr", "year": 2004, "duration": "3:30", "bpm": 90, "cover_url": "", "spotify_url": "#none", "reason": "Turkce rapin sert hiti"},
    {"id": "s208", "name": "Sirtimda Yuku", "artist": "Ceza", "album": "Rapstar", "genres": ["turkce_rap"], "moods": ["motivasyon", "enerjik"], "activities": ["spor", "gym"], "language": "tr", "year": 2006, "duration": "4:00", "bpm": 95, "cover_url": "", "spotify_url": "#none", "reason": "Turkce rap motivasyon sarkisi"},
    {"id": "s209", "name": "Gozlerin", "artist": "Ferdi Tayfur", "album": "Gozlerin", "genres": ["arabesk"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1985, "duration": "4:10", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Arabesk romantik klasiği"},
    {"id": "s210", "name": "Yorgun Demokrat", "artist": "Baris Manco", "album": "Yorgun Demokrat", "genres": ["anadolu_rock"], "moods": ["nostaljik", "mutlu"], "activities": ["araba", "gece"], "language": "tr", "year": 1975, "duration": "3:55", "bpm": 102, "cover_url": "", "spotify_url": "#none", "reason": "Baris Manco klasiği"},
    {"id": "s211", "name": "Yalan Dunya", "artist": "Cem Karaca", "album": "Cem Karaca", "genres": ["anadolu_rock"], "moods": ["sinirli", "motivasyon"], "activities": ["araba"], "language": "tr", "year": 1976, "duration": "3:45", "bpm": 110, "cover_url": "", "spotify_url": "#none", "reason": "Anadolu rockin asi esi"},
    {"id": "s212", "name": "Kucuk Sevgilim", "artist": "Gripin", "album": "Gripin", "genres": ["turkce_rock", "pop"], "moods": ["romantik", "mutlu"], "activities": ["araba", "yazlik"], "language": "tr", "year": 2007, "duration": "3:30", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Pop-rock ask sarkisi"},
    {"id": "s213", "name": "Son Aralik", "artist": "Pinhani", "album": "Zor", "genres": ["turkce_rock", "indie"], "moods": ["sakin", "melankolik"], "activities": ["kahve", "gece"], "language": "tr", "year": 2009, "duration": "3:20", "bpm": 70, "cover_url": "", "spotify_url": "#none", "reason": "Pinhani'nin sakin eseri"},

    # ========================
    # EK LO-FI / ODAK / KOD
    # ========================
    {"id": "s220", "name": "Lofi Study", "artist": "ChilledCow", "genres": ["lofi"], "moods": ["sakin"], "activities": ["ders", "odak", "kod"], "language": "en", "year": 2020, "duration": "3:15", "bpm": 75, "cover_url": "", "spotify_url": "#none", "reason": "Lo-fi ders muzigi"},
    {"id": "s221", "name": "Snowfall", "artist": "Øneheart & Reidenshi", "genres": ["lofi", "ambient"], "moods": ["sakin", "melankolik"], "activities": ["ders", "uyku", "yagmur"], "language": "en", "year": 2022, "duration": "2:30", "bpm": 70, "cover_url": "", "spotify_url": "#none", "reason": "Sakinlestirici lo-fi"},
    {"id": "s222", "name": "Still Corner", "artist": "Still Corners", "genres": ["indie", "synthpop"], "moods": ["sakin", "nostaljik"], "activities": ["gece", "araba", "yagmur"], "language": "en", "year": 2018, "duration": "3:40", "bpm": 80, "cover_url": "", "spotify_url": "#none", "reason": "Dreamy indie pop"},

    # ========================
    # EK MOTIVASYON / SPOR
    # ========================
    {"id": "s230", "name": "Eye of the Tiger", "artist": "Survivor", "album": "Eye of the Tiger", "genres": ["rock"], "moods": ["motivasyon", "enerjik"], "activities": ["spor", "gym", "kosu"], "language": "en", "year": 1982, "duration": "4:05", "bpm": 136, "cover_url": "", "spotify_url": "#none", "reason": "Motivasyon klasiği"},
    {"id": "s231", "name": "Thunderstruck", "artist": "AC/DC", "album": "The Razors Edge", "genres": ["rock", "metal"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "gym", "parti"], "language": "en", "year": 1990, "duration": "4:52", "bpm": 134, "cover_url": "", "spotify_url": "#none", "reason": "Enerji veren rock klasiği"},

    # ========================
    # EK SANATCI SARKILARI (minimum 5 hedefi)
    # ========================
    # Queen
    {"id": "s301", "name": "We Are the Champions", "artist": "Queen", "album": "News of the World", "genres": ["rock"], "moods": ["motivasyon", "epik"], "activities": ["spor", "parti"], "language": "en", "year": 1977, "duration": "2:59", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Motivasyon klasiği"},
    {"id": "s302", "name": "Somebody to Love", "artist": "Queen", "album": "A Day at the Races", "genres": ["rock"], "moods": ["mutlu", "enerjik"], "activities": ["araba", "parti"], "language": "en", "year": 1976, "duration": "4:56", "bpm": 144, "cover_url": "", "spotify_url": "#none", "reason": "Queen'in guclu vokali"},
    {"id": "s303", "name": "Don't Stop Me Now", "artist": "Queen", "album": "Jazz", "genres": ["rock"], "moods": ["mutlu", "enerjik", "motivasyon"], "activities": ["parti", "spor", "araba"], "language": "en", "year": 1978, "duration": "3:29", "bpm": 156, "cover_url": "", "spotify_url": "#none", "reason": "Queen'in en eglenceli sarkisi"},

    # Led Zeppelin
    {"id": "s305", "name": "Kashmir", "artist": "Led Zeppelin", "album": "Physical Graffiti", "genres": ["rock"], "moods": ["epik", "sakin"], "activities": ["araba", "gece"], "language": "en", "year": 1975, "duration": "8:31", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Led Zeppelin'in epik basyapidi"},
    {"id": "s306", "name": "Whole Lotta Love", "artist": "Led Zeppelin", "album": "Led Zeppelin II", "genres": ["rock"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "parti"], "language": "en", "year": 1969, "duration": "5:33", "bpm": 140, "cover_url": "", "spotify_url": "#none", "reason": "Rock klasiği"},

    # Metallica (+ Master of Puppets zaten var)
    {"id": "s308", "name": "Nothing Else Matters", "artist": "Metallica", "album": "Metallica", "genres": ["metal", "rock"], "moods": ["melankolik", "sakin"], "activities": ["gece", "yagmur"], "language": "en", "year": 1992, "duration": "6:28", "bpm": 138, "cover_url": "", "spotify_url": "#none", "reason": "Metallica'nin duygusal yuzu"},
    {"id": "s309", "name": "The Unforgiven", "artist": "Metallica", "album": "Metallica", "genres": ["metal", "rock"], "moods": ["melankolik", "sinirli"], "activities": ["gece"], "language": "en", "year": 1991, "duration": "6:27", "bpm": 152, "cover_url": "", "spotify_url": "#none", "reason": "Metallica'nin ikonik baladi"},
    {"id": "s310", "name": "One", "artist": "Metallica", "album": "...And Justice for All", "genres": ["metal"], "moods": ["sinirli", "enerjik"], "activities": ["spor", "gym"], "language": "en", "year": 1988, "duration": "7:44", "bpm": 167, "cover_url": "", "spotify_url": "#none", "reason": "Metallica'nin progresif basyapidi"},

    # AC/DC
    {"id": "s312", "name": "Highway to Hell", "artist": "AC/DC", "album": "Highway to Hell", "genres": ["rock"], "moods": ["enerjik", "mutlu"], "activities": ["araba", "parti", "spor"], "language": "en", "year": 1979, "duration": "3:28", "bpm": 116, "cover_url": "", "spotify_url": "#none", "reason": "AC/DC klasiği"},
    {"id": "s313", "name": "TNT", "artist": "AC/DC", "album": "TNT", "genres": ["rock"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "parti"], "language": "en", "year": 1975, "duration": "3:34", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "AC/DC'nin patlayici sarkisi"},
    {"id": "s314", "name": "Dirty Deeds Done Dirt Cheap", "artist": "AC/DC", "album": "Dirty Deeds Done Dirt Cheap", "genres": ["rock"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "araba"], "language": "en", "year": 1976, "duration": "4:11", "bpm": 132, "cover_url": "", "spotify_url": "#none", "reason": "AC/DC'nin sert rock sarkisi"},

    # The Beatles
    {"id": "s316", "name": "Let It Be", "artist": "The Beatles", "album": "Let It Be", "genres": ["rock", "pop"], "moods": ["sakin", "uzgun", "nostaljik"], "activities": ["gece", "yagmur"], "language": "en", "year": 1970, "duration": "4:03", "bpm": 79, "cover_url": "", "spotify_url": "#none", "reason": "Beatles'in huzur verici klasiği"},
    {"id": "s317", "name": "Come Together", "artist": "The Beatles", "album": "Abbey Road", "genres": ["rock"], "moods": ["sakin", "enerjik"], "activities": ["araba", "gece"], "language": "en", "year": 1969, "duration": "4:19", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Beatles'in ikonik sarkisi"},
    {"id": "s318", "name": "Hey Jude", "artist": "The Beatles", "album": "Single", "genres": ["rock", "pop"], "moods": ["mutlu", "nostaljik"], "activities": ["araba", "parti"], "language": "en", "year": 1968, "duration": "7:11", "bpm": 152, "cover_url": "", "spotify_url": "#none", "reason": "Beatles'in en unlu sarkisi"},

    # Adele
    {"id": "s320", "name": "Hello", "artist": "Adele", "album": "25", "genres": ["pop", "soul"], "moods": ["uzgun", "nostaljik"], "activities": ["gece", "yagmur"], "language": "en", "year": 2015, "duration": "4:55", "bpm": 68, "cover_url": "", "spotify_url": "#none", "reason": "Adele'in guclu vokali"},
    {"id": "s321", "name": "Set Fire to the Rain", "artist": "Adele", "album": "21", "genres": ["pop", "soul"], "moods": ["uzgun", "enerjik"], "activities": ["gece"], "language": "en", "year": 2011, "duration": "4:02", "bpm": 108, "cover_url": "", "spotify_url": "#none", "reason": "Adele'in dramatik sarkisi"},
    {"id": "s322", "name": "Chasing Pavements", "artist": "Adele", "album": "19", "genres": ["pop", "soul"], "moods": ["romantik", "uzgun"], "activities": ["gece", "araba"], "language": "en", "year": 2008, "duration": "3:30", "bpm": 132, "cover_url": "", "spotify_url": "#none", "reason": "Adele'in romantik baladi"},

    # The Weeknd
    {"id": "s324", "name": "Starboy", "artist": "The Weeknd", "album": "Starboy", "genres": ["rnb", "pop"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "araba"], "language": "en", "year": 2016, "duration": "3:50", "bpm": 192, "cover_url": "", "spotify_url": "#none", "reason": "The Weeknd'in populer hiti"},
    {"id": "s325", "name": "Save Your Tears", "artist": "The Weeknd", "album": "After Hours", "genres": ["pop", "synthpop"], "moods": ["uzgun", "nostaljik"], "activities": ["gece", "araba"], "language": "en", "year": 2020, "duration": "3:36", "bpm": 118, "cover_url": "", "spotify_url": "#none", "reason": "The Weeknd'in duygusal sarkisi"},
    {"id": "s326", "name": "Die For You", "artist": "The Weeknd", "album": "Starboy", "genres": ["rnb", "pop"], "moods": ["romantik", "uzgun"], "activities": ["gece"], "language": "en", "year": 2016, "duration": "4:01", "bpm": 111, "cover_url": "", "spotify_url": "#none", "reason": "The Weeknd'in romantik sarkisi"},

    # Ed Sheeran
    {"id": "s328", "name": "Photograph", "artist": "Ed Sheeran", "album": "x", "genres": ["pop"], "moods": ["romantik", "nostaljik"], "activities": ["gece", "kahve"], "language": "en", "year": 2014, "duration": "4:19", "bpm": 108, "cover_url": "", "spotify_url": "#none", "reason": "Ed Sheeran'in romantik klasiği"},
    {"id": "s329", "name": "Castle on the Hill", "artist": "Ed Sheeran", "album": "Divide", "genres": ["pop"], "moods": ["nostaljik", "enerjik"], "activities": ["araba", "yazlik"], "language": "en", "year": 2017, "duration": "4:22", "bpm": 136, "cover_url": "", "spotify_url": "#none", "reason": "Ed Sheeran'in nostaljik sarkisi"},

    # Avicii
    {"id": "s331", "name": "Waiting for Love", "artist": "Avicii", "album": "Stories", "genres": ["elektronik", "edm"], "moods": ["mutlu", "enerjik", "motivasyon"], "activities": ["spor", "parti"], "language": "en", "year": 2015, "duration": "3:47", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "Avicii'nin mutlu sarkisi"},

    # Dua Lipa
    {"id": "s333", "name": "Don't Start Now", "artist": "Dua Lipa", "album": "Future Nostalgia", "genres": ["pop", "disko"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "spor", "araba"], "language": "en", "year": 2019, "duration": "3:03", "bpm": 124, "cover_url": "", "spotify_url": "#none", "reason": "Dua Lipa'nin dans hiti"},
    {"id": "s334", "name": "New Rules", "artist": "Dua Lipa", "album": "Dua Lipa", "genres": ["pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "en", "year": 2017, "duration": "3:29", "bpm": 116, "cover_url": "", "spotify_url": "#none", "reason": "Dua Lipa'nin guclu sarkisi"},
    {"id": "s335", "name": "Physical", "artist": "Dua Lipa", "album": "Future Nostalgia", "genres": ["pop", "disko"], "moods": ["enerjik", "mutlu"], "activities": ["spor", "parti"], "language": "en", "year": 2020, "duration": "3:04", "bpm": 148, "cover_url": "", "spotify_url": "#none", "reason": "Dua Lipa'nin enerjik sarkisi"},
    {"id": "s336", "name": "Love Again", "artist": "Dua Lipa", "album": "Future Nostalgia", "genres": ["pop", "disko"], "moods": ["mutlu", "romantik"], "activities": ["araba", "parti"], "language": "en", "year": 2021, "duration": "3:30", "bpm": 118, "cover_url": "", "spotify_url": "#none", "reason": "Dua Lipa'nin nostaljik sarkisi"},

    # Harry Styles
    {"id": "s338", "name": "Adore You", "artist": "Harry Styles", "album": "Fine Line", "genres": ["pop"], "moods": ["romantik", "mutlu"], "activities": ["araba", "kahve"], "language": "en", "year": 2019, "duration": "3:27", "bpm": 100, "cover_url": "", "spotify_url": "#none", "reason": "Harry Styles'in romantik sarkisi"},
    {"id": "s339", "name": "As It Was", "artist": "Harry Styles", "album": "Harry's House", "genres": ["pop"], "moods": ["nostaljik", "melankolik"], "activities": ["araba", "gece"], "language": "en", "year": 2022, "duration": "2:47", "bpm": 174, "cover_url": "", "spotify_url": "#none", "reason": "Harry Styles'in en buyuk hiti"},
    {"id": "s340", "name": "Sign of the Times", "artist": "Harry Styles", "album": "Harry Styles", "genres": ["pop", "rock"], "moods": ["melankolik", "epik"], "activities": ["gece", "yagmur"], "language": "en", "year": 2017, "duration": "5:40", "bpm": 62, "cover_url": "", "spotify_url": "#none", "reason": "Harry Styles'in duygusal sarkisi"},
    {"id": "s341", "name": "Falling", "artist": "Harry Styles", "album": "Fine Line", "genres": ["pop"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "en", "year": 2019, "duration": "4:01", "bpm": 74, "cover_url": "", "spotify_url": "#none", "reason": "Harry Styles'in huzunlu baladi"},

    # Eminem
    {"id": "s343", "name": "The Real Slim Shady", "artist": "Eminem", "album": "The Marshall Mathers LP", "genres": ["rap"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "spor"], "language": "en", "year": 2000, "duration": "4:44", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Eminem'in ikonik sarkisi"},
    {"id": "s344", "name": "Stan", "artist": "Eminem", "album": "The Marshall Mathers LP", "genres": ["rap"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "en", "year": 2000, "duration": "6:44", "bpm": 79, "cover_url": "", "spotify_url": "#none", "reason": "Eminem'in duygusal basyapidi"},
    {"id": "s345", "name": "Without Me", "artist": "Eminem", "album": "The Eminem Show", "genres": ["rap"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "spor"], "language": "en", "year": 2002, "duration": "4:50", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Eminem'in eglenceli sarkisi"},
    {"id": "s346", "name": "Not Afraid", "artist": "Eminem", "album": "Recovery", "genres": ["rap"], "moods": ["motivasyon", "guclu"], "activities": ["spor", "gym"], "language": "en", "year": 2010, "duration": "4:08", "bpm": 86, "cover_url": "", "spotify_url": "#none", "reason": "Eminem'in motivasyon sarkisi"},

    # Kendrick Lamar
    {"id": "s348", "name": "DNA.", "artist": "Kendrick Lamar", "album": "DAMN.", "genres": ["rap"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "en", "year": 2017, "duration": "3:06", "bpm": 150, "cover_url": "", "spotify_url": "#none", "reason": "Kendrick Lamar'in sert sarkisi"},
    {"id": "s349", "name": "Alright", "artist": "Kendrick Lamar", "album": "To Pimp a Butterfly", "genres": ["rap", "jazz"], "moods": ["motivasyon", "mutlu"], "activities": ["araba", "spor"], "language": "en", "year": 2015, "duration": "3:39", "bpm": 112, "cover_url": "", "spotify_url": "#none", "reason": "Kendrick Lamar'in umut sarkisi"},
    {"id": "s350", "name": "Money Trees", "artist": "Kendrick Lamar", "album": "good kid, m.A.A.d city", "genres": ["rap"], "moods": ["sakin", "nostaljik"], "activities": ["gece", "kod"], "language": "en", "year": 2012, "duration": "6:37", "bpm": 72, "cover_url": "", "spotify_url": "#none", "reason": "Kendrick Lamar'in sakin rap eseri"},
    {"id": "s351", "name": "Swimming Pools", "artist": "Kendrick Lamar", "album": "good kid, m.A.A.d city", "genres": ["rap"], "moods": ["sakin", "melankolik"], "activities": ["gece"], "language": "en", "year": 2012, "duration": "4:21", "bpm": 74, "cover_url": "", "spotify_url": "#none", "reason": "Kendrick Lamar'in derin sarkisi"},

    # Drake
    {"id": "s353", "name": "One Dance", "artist": "Drake", "album": "Views", "genres": ["rap", "pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "en", "year": 2016, "duration": "2:53", "bpm": 118, "cover_url": "", "spotify_url": "#none", "reason": "Drake'in dans hiti"},
    {"id": "s354", "name": "Hotline Bling", "artist": "Drake", "album": "Views", "genres": ["rap", "rnb"], "moods": ["nostaljik", "melankolik"], "activities": ["gece", "araba"], "language": "en", "year": 2015, "duration": "4:27", "bpm": 135, "cover_url": "", "spotify_url": "#none", "reason": "Drake'in nostaljik sarkisi"},
    {"id": "s355", "name": "In My Feelings", "artist": "Drake", "album": "Scorpion", "genres": ["rap", "rnb"], "moods": ["mutlu", "romantik"], "activities": ["parti", "araba"], "language": "en", "year": 2018, "duration": "3:37", "bpm": 92, "cover_url": "", "spotify_url": "#none", "reason": "Drake'in romantik sarkisi"},
    {"id": "s356", "name": "Passionfruit", "artist": "Drake", "album": "More Life", "genres": ["rap", "rnb"], "moods": ["sakin", "romantik"], "activities": ["gece", "chill"], "language": "en", "year": 2017, "duration": "4:58", "bpm": 112, "cover_url": "", "spotify_url": "#none", "reason": "Drake'in sakin sarkisi"},

    # Sezen Aksu
    {"id": "s358", "name": "Gulumse", "artist": "Sezen Aksu", "album": "Gulumse", "genres": ["turkce_pop"], "moods": ["mutlu", "nostaljik"], "activities": ["araba", "parti"], "language": "tr", "year": 1991, "duration": "3:45", "bpm": 110, "cover_url": "", "spotify_url": "#none", "reason": "Sezen Aksu'nun efsane sarkisi"},
    {"id": "s359", "name": "Hadi Bakalim", "artist": "Sezen Aksu", "album": "Deniz Yildizi", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "tr", "year": 2008, "duration": "3:20", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Sezen Aksu'nun eglenceli sarkisi"},
    {"id": "s360", "name": "Yanlizlik Senfonisi", "artist": "Sezen Aksu", "album": "Gulumse", "genres": ["turkce_pop"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1991, "duration": "4:15", "bpm": 85, "cover_url": "", "spotify_url": "#none", "reason": "Sezen Aksu'nun duygusal sarkisi"},

    # Tarkan
    {"id": "s362", "name": "Simarik", "artist": "Tarkan", "album": "Olurum Sana", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik", "romantik"], "activities": ["parti", "araba"], "language": "tr", "year": 1997, "duration": "3:30", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Tarkan'in dunyayi sarsan hiti"},
    {"id": "s363", "name": "Dudu", "artist": "Tarkan", "album": "Dudu", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "tr", "year": 2003, "duration": "3:40", "bpm": 125, "cover_url": "", "spotify_url": "#none", "reason": "Tarkan'in dans hiti"},
    {"id": "s364", "name": "Yine Sensiz", "artist": "Tarkan", "album": "Yine Sensiz", "genres": ["turkce_pop"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1994, "duration": "4:20", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Tarkan'in romantik baladi"},
    {"id": "s365", "name": "Kuzu Kuzu", "artist": "Tarkan", "album": "Karma", "genres": ["turkce_pop"], "moods": ["romantik", "enerjik"], "activities": ["araba", "parti"], "language": "tr", "year": 2001, "duration": "3:55", "bpm": 115, "cover_url": "", "spotify_url": "#none", "reason": "Tarkan'in populer sarkisi"},

    # Mor ve Otesi
    {"id": "s367", "name": "Sevda Cicegi", "artist": "Mor ve Otesi", "album": "Dunya Yalan Soyluyor", "genres": ["turkce_rock"], "moods": ["enerjik", "mutlu"], "activities": ["araba", "spor"], "language": "tr", "year": 2004, "duration": "3:45", "bpm": 130, "cover_url": "", "spotify_url": "#none", "reason": "Mor ve Otesi'nin_hit sarkisi"},

    # Sebnem Ferah
    {"id": "s369", "name": "Yagmurla Gelen", "artist": "Sebnem Ferah", "album": "Artik Kisa Seyler Soyluyorum", "genres": ["turkce_rock"], "moods": ["uzgun", "sakin"], "activities": ["yagmur", "gece"], "language": "tr", "year": 2005, "duration": "4:20", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Sebnem Ferah'in duygusal sarkisi"},
    {"id": "s370", "name": "Günün Yorgunluğu", "artist": "Sebnem Ferah", "album": "Artik Kisa Seyler Soyluyorum", "genres": ["turkce_rock"], "moods": ["melankolik", "sakin"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1999, "duration": "4:10", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Sebnem Ferah'in huzur sarkisi"},
    {"id": "s371", "name": "Bibir", "artist": "Sebnem Ferah", "album": "Kirik", "genres": ["turkce_rock"], "moods": ["enerjik", "romantik"], "activities": ["araba"], "language": "tr", "year": 2017, "duration": "3:30", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Sebnem Ferah'in modern sarkisi"},

    # Nirvana
    {"id": "s373", "name": "Come as You Are", "artist": "Nirvana", "album": "Nevermind", "genres": ["rock", "grunge"], "moods": ["sakin", "melankolik"], "activities": ["gece", "araba"], "language": "en", "year": 1991, "duration": "3:39", "bpm": 95, "cover_url": "", "spotify_url": "#none", "reason": "Nirvana'nin ikonik riff'i"},
    {"id": "s374", "name": "Heart-Shaped Box", "artist": "Nirvana", "album": "In Utero", "genres": ["rock", "grunge"], "moods": ["sinirli", "melankolik"], "activities": ["spor", "gece"], "language": "en", "year": 1993, "duration": "4:41", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Nirvana'nin karanlik sarkisi"},
    {"id": "s375", "name": "Lithium", "artist": "Nirvana", "album": "Nevermind", "genres": ["rock", "grunge"], "moods": ["enerjik", "sinirli"], "activities": ["spor"], "language": "en", "year": 1991, "duration": "4:17", "bpm": 118, "cover_url": "", "spotify_url": "#none", "reason": "Nirvana'nin enerjik sarkisi"},
    {"id": "s376", "name": "All Apologies", "artist": "Nirvana", "album": "In Utero", "genres": ["rock", "grunge"], "moods": ["sakin", "melankolik"], "activities": ["gece", "yagmur"], "language": "en", "year": 1993, "duration": "3:50", "bpm": 98, "cover_url": "", "spotify_url": "#none", "reason": "Nirvana'nin huzurlu veda sarkisi"},

    # Pink Floyd
    {"id": "s378", "name": "Wish You Were Here", "artist": "Pink Floyd", "album": "Wish You Were Here", "genres": ["rock"], "moods": ["melankolik", "nostaljik"], "activities": ["gece", "yagmur"], "language": "en", "year": 1975, "duration": "5:34", "bpm": 68, "cover_url": "", "spotify_url": "#none", "reason": "Pink Floyd'un huzurlu klasiği"},
    {"id": "s379", "name": "Money", "artist": "Pink Floyd", "album": "The Dark Side of the Moon", "genres": ["rock"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "araba"], "language": "en", "year": 1973, "duration": "6:23", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Pink Floyd'un ritim klasiği"},
    {"id": "s380", "name": "Another Brick in the Wall", "artist": "Pink Floyd", "album": "The Wall", "genres": ["rock"], "moods": ["sinirli", "enerjik"], "activities": ["spor", "parti"], "language": "en", "year": 1979, "duration": "3:59", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Pink Floyd'un asi klasiği"},
    {"id": "s381", "name": "Time", "artist": "Pink Floyd", "album": "The Dark Side of the Moon", "genres": ["rock"], "moods": ["melankolik", "nostaljik"], "activities": ["gece", "ders"], "language": "en", "year": 1973, "duration": "6:59", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Pink Floyd'un zaman temali basyapidi"},

    # Eagles
    {"id": "s383", "name": "Take It Easy", "artist": "Eagles", "album": "Eagles", "genres": ["rock", "country"], "moods": ["mutlu", "sakin"], "activities": ["araba", "yazlik"], "language": "en", "year": 1972, "duration": "3:31", "bpm": 132, "cover_url": "", "spotify_url": "#none", "reason": "Eagles'in rahat sarkisi"},
    {"id": "s384", "name": "Desperado", "artist": "Eagles", "album": "Desperado", "genres": ["rock", "country"], "moods": ["uzgun", "sakin"], "activities": ["gece", "yagmur"], "language": "en", "year": 1973, "duration": "3:33", "bpm": 90, "cover_url": "", "spotify_url": "#none", "reason": "Eagles'in duygusal klasiği"},
    {"id": "s385", "name": "Life in the Fast Lane", "artist": "Eagles", "album": "Hotel California", "genres": ["rock"], "moods": ["enerjik", "sinirli"], "activities": ["araba", "spor"], "language": "en", "year": 1976, "duration": "4:46", "bpm": 152, "cover_url": "", "spotify_url": "#none", "reason": "Eagles'in hizli sarkisi"},
    {"id": "s386", "name": "New Kid in Town", "artist": "Eagles", "album": "Hotel California", "genres": ["rock", "country"], "moods": ["nostaljik", "sakin"], "activities": ["araba", "gece"], "language": "en", "year": 1976, "duration": "5:04", "bpm": 103, "cover_url": "", "spotify_url": "#none", "reason": "Eagles'in huzurlu sarkisi"},

    # Iron Maiden
    {"id": "s388", "name": "The Trooper", "artist": "Iron Maiden", "album": "Piece of Mind", "genres": ["metal"], "moods": ["enerjik", "epik"], "activities": ["spor", "gym"], "language": "en", "year": 1983, "duration": "4:10", "bpm": 160, "cover_url": "", "spotify_url": "#none", "reason": "Iron Maiden'in klasiği"},
    {"id": "s389", "name": "Hallowed Be Thy Name", "artist": "Iron Maiden", "album": "The Number of the Beast", "genres": ["metal"], "moods": ["epik", "melankolik"], "activities": ["gece"], "language": "en", "year": 1982, "duration": "7:11", "bpm": 132, "cover_url": "", "spotify_url": "#none", "reason": "Iron Maiden'in epik basyapidi"},
    {"id": "s390", "name": "Run to the Hills", "artist": "Iron Maiden", "album": "The Number of the Beast", "genres": ["metal"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "en", "year": 1982, "duration": "3:50", "bpm": 146, "cover_url": "", "spotify_url": "#none", "reason": "Iron Maiden'in hizli sarkisi"},
    {"id": "s391", "name": "Number of the Beast", "artist": "Iron Maiden", "album": "The Number of the Beast", "genres": ["metal"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "en", "year": 1982, "duration": "4:49", "bpm": 154, "cover_url": "", "spotify_url": "#none", "reason": "Iron Maiden'in ikonik sarkisi"},

    # Black Sabbath
    {"id": "s393", "name": "Iron Man", "artist": "Black Sabbath", "album": "Paranoid", "genres": ["metal"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "en", "year": 1970, "duration": "5:55", "bpm": 168, "cover_url": "", "spotify_url": "#none", "reason": "Black Sabbath'in klasiği"},
    {"id": "s394", "name": "War Pigs", "artist": "Black Sabbath", "album": "Paranoid", "genres": ["metal"], "moods": ["sinirli", "epik"], "activities": ["spor"], "language": "en", "year": 1970, "duration": "7:57", "bpm": 108, "cover_url": "", "spotify_url": "#none", "reason": "Black Sabbath'in asi sarkisi"},
    {"id": "s395", "name": "Sweet Leaf", "artist": "Black Sabbath", "album": "Master of Reality", "genres": ["metal"], "moods": ["sakin", "enerjik"], "activities": ["araba"], "language": "en", "year": 1971, "duration": "5:04", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Black Sabbath'in rahat sarkisi"},
    {"id": "s396", "name": "Heaven and Hell", "artist": "Black Sabbath", "album": "Heaven and Hell", "genres": ["metal"], "moods": ["epik", "enerjik"], "activities": ["spor", "gece"], "language": "en", "year": 1980, "duration": "6:56", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "Black Sabbath'in epik sarkisi"},

    # Green Day
    {"id": "s398", "name": "Boulevard of Broken Dreams", "artist": "Green Day", "album": "American Idiot", "genres": ["punk", "rock"], "moods": ["melankolik", "sinirli"], "activities": ["araba", "gece"], "language": "en", "year": 2004, "duration": "4:20", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": "Green Day'in ikonik sarkisi"},
    {"id": "s399", "name": "American Idiot", "artist": "Green Day", "album": "American Idiot", "genres": ["punk", "rock"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "en", "year": 2004, "duration": "2:57", "bpm": 165, "cover_url": "", "spotify_url": "#none", "reason": "Green Day'in asi sarkisi"},
    {"id": "s400", "name": "Wake Me Up When September Ends", "artist": "Green Day", "album": "American Idiot", "genres": ["punk", "rock"], "moods": ["uzgun", "melankolik"], "activities": ["yagmur", "gece"], "language": "en", "year": 2005, "duration": "4:45", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Green Day'in duygusal sarkisi"},
    {"id": "s401", "name": "21 Guns", "artist": "Green Day", "album": "21st Century Breakdown", "genres": ["punk", "rock"], "moods": ["melankolik", "motivasyon"], "activities": ["gece"], "language": "en", "year": 2009, "duration": "5:21", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": "Green Day'in motivasyon sarkisi"},

    # Arctic Monkeys
    {"id": "s403", "name": "Arabella", "artist": "Arctic Monkeys", "album": "AM", "genres": ["indie", "rock"], "moods": ["enerjik", "romantik"], "activities": ["araba", "gece"], "language": "en", "year": 2013, "duration": "3:27", "bpm": 104, "cover_url": "", "spotify_url": "#none", "reason": "Arctic Monkeys'in rock sarkisi"},
    {"id": "s404", "name": "505", "artist": "Arctic Monkeys", "album": "Favourite Worst Nightmare", "genres": ["indie", "rock"], "moods": ["melankolik", "romantik"], "activities": ["gece", "yagmur"], "language": "en", "year": 2007, "duration": "4:13", "bpm": 148, "cover_url": "", "spotify_url": "#none", "reason": "Arctic Monkeys'in duygusal sarkisi"},
    {"id": "s405", "name": "R U Mine?", "artist": "Arctic Monkeys", "album": "AM", "genres": ["indie", "rock"], "moods": ["enerjik", "romantik"], "activities": ["spor", "araba"], "language": "en", "year": 2013, "duration": "3:20", "bpm": 130, "cover_url": "", "spotify_url": "#none", "reason": "Arctic Monkeys'in enerjik sarkisi"},
    {"id": "s406", "name": "Fluorescent Adolescent", "artist": "Arctic Monkeys", "album": "Favourite Worst Nightmare", "genres": ["indie", "rock"], "moods": ["mutlu", "nostaljik"], "activities": ["araba", "parti"], "language": "en", "year": 2007, "duration": "2:57", "bpm": 160, "cover_url": "", "spotify_url": "#none", "reason": "Arctic Monkeys'in nostaljik sarkisi"},

    # Tame Impala
    {"id": "s408", "name": "Borderline", "artist": "Tame Impala", "album": "The Slow Rush", "genres": ["indie", "psychedelik"], "moods": ["mutlu", "sakin"], "activities": ["araba", "yazlik"], "language": "en", "year": 2020, "duration": "3:58", "bpm": 110, "cover_url": "", "spotify_url": "#none", "reason": "Tame Impala'nin modern sarkisi"},
    {"id": "s409", "name": "Let It Happen", "artist": "Tame Impala", "album": "Currents", "genres": ["indie", "psychedelik"], "moods": ["sakin", "enerjik"], "activities": ["araba", "gece"], "language": "en", "year": 2015, "duration": "7:47", "bpm": 126, "cover_url": "", "spotify_url": "#none", "reason": "Tame Impala'nin uzun epik sarkisi"},
    {"id": "s410", "name": "Feels Like We Only Go Backwards", "artist": "Tame Impala", "album": "Lonerism", "genres": ["indie", "psychedelik"], "moods": ["melankolik", "sakin"], "activities": ["gece", "yagmur"], "language": "en", "year": 2012, "duration": "3:12", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Tame Impala'nin duygusal sarkisi"},
    {"id": "s411", "name": "New Person, Same Old Mistakes", "artist": "Tame Impala", "album": "Currents", "genres": ["indie", "psychedelik"], "moods": ["sakin", "melankolik"], "activities": ["gece", "chill"], "language": "en", "year": 2015, "duration": "6:03", "bpm": 100, "cover_url": "", "spotify_url": "#none", "reason": "Tame Impala'nin huzurlu sarkisi"},

    # Miles Davis
    {"id": "s413", "name": "Blue in Green", "artist": "Miles Davis", "album": "Kind of Blue", "genres": ["jazz"], "moods": ["sakin", "melankolik"], "activities": ["kahve", "gece"], "language": "en", "year": 1959, "duration": "5:27", "bpm": 80, "cover_url": "", "spotify_url": "#none", "reason": "Jazz'in en duygusal eseri"},
    {"id": "s414", "name": "Freddie Freeloader", "artist": "Miles Davis", "album": "Kind of Blue", "genres": ["jazz"], "moods": ["mutlu", "sakin"], "activities": ["kahve", "ders"], "language": "en", "year": 1959, "duration": "9:46", "bpm": 132, "cover_url": "", "spotify_url": "#none", "reason": "Jazz'in en eglenceli eseri"},
    {"id": "s415", "name": "All Blues", "artist": "Miles Davis", "album": "Kind of Blue", "genres": ["jazz"], "moods": ["sakin", "romantik"], "activities": ["gece", "kahve"], "language": "en", "year": 1959, "duration": "11:33", "bpm": 64, "cover_url": "", "spotify_url": "#none", "reason": "Miles Davis'in blues sarkisi"},
    {"id": "s416", "name": "Summertime", "artist": "Miles Davis", "album": "Porgy and Bess", "genres": ["jazz"], "moods": ["sakin", "romantik"], "activities": ["sabah", "kahve"], "language": "en", "year": 1958, "duration": "3:55", "bpm": 92, "cover_url": "", "spotify_url": "#none", "reason": "Jazz klasiği"},

    # John Legend
    {"id": "s418", "name": "Used to Love U", "artist": "John Legend", "album": "Get Lifted", "genres": ["rnb", "soul"], "moods": ["uzgun", "romantik"], "activities": ["gece", "yagmur"], "language": "en", "year": 2004, "duration": "4:04", "bpm": 95, "cover_url": "", "spotify_url": "#none", "reason": "John Legend'in duygusal sarkisi"},
    {"id": "s419", "name": "Ordinary People", "artist": "John Legend", "album": "Get Lifted", "genres": ["rnb", "soul"], "moods": ["romantik", "sakin"], "activities": ["gece", "kahve"], "language": "en", "year": 2004, "duration": "4:41", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": "John Legend'in sakin klasiği"},
    {"id": "s420", "name": "Love Me Now", "artist": "John Legend", "album": "Darkness and Light", "genres": ["pop", "rnb"], "moods": ["romantik", "enerjik"], "activities": ["parti", "araba"], "language": "en", "year": 2016, "duration": "3:30", "bpm": 107, "cover_url": "", "spotify_url": "#none", "reason": "John Legend'in ask sarkisi"},
    {"id": "s421", "name": "Save Room", "artist": "John Legend", "album": "Once Again", "genres": ["soul", "pop"], "moods": ["romantik", "sakin"], "activities": ["kahve", "gece"], "language": "en", "year": 2006, "duration": "3:52", "bpm": 92, "cover_url": "", "spotify_url": "#none", "reason": "John Legend'in soul sarkisi"},

    # ========================
    # KALAN SANATCI TAMAMLAMALARI
    # ========================
    # Travis Scott
    {"id": "s500", "name": "SICKO MODE", "artist": "Travis Scott", "album": "Astroworld", "genres": ["rap", "trap"], "moods": ["enerjik", "sinirli"], "activities": ["parti", "oyun"], "language": "en", "year": 2018, "duration": "5:12", "bpm": 155, "cover_url": "", "spotify_url": "#none", "reason": "Travis Scott'in hit sarkisi"},
    {"id": "s501", "name": "goosebumps", "artist": "Travis Scott", "album": "Birds in the Trap Sing McKnight", "genres": ["rap", "trap"], "moods": ["sakin", "melankolik"], "activities": ["gece", "kod"], "language": "en", "year": 2016, "duration": "4:26", "bpm": 130, "cover_url": "", "spotify_url": "#none", "reason": "Travis Scott'in atmosferik sarkisi"},
    {"id": "s502", "name": "STARGAZING", "artist": "Travis Scott", "album": "Astroworld", "genres": ["rap", "trap"], "moods": ["enerjik", "epik"], "activities": ["spor", "parti"], "language": "en", "year": 2018, "duration": "2:56", "bpm": 130, "cover_url": "", "spotify_url": "#none", "reason": "Travis Scott'in enerjik opener'i"},
    {"id": "s503", "name": "Antidote", "artist": "Travis Scott", "album": "Rodeo", "genres": ["rap", "trap"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "araba"], "language": "en", "year": 2015, "duration": "3:28", "bpm": 135, "cover_url": "", "spotify_url": "#none", "reason": "Travis Scott'in parti sarkisi"},
    {"id": "s504", "name": "HIGHEST IN THE ROOM", "artist": "Travis Scott", "album": "Jackboys", "genres": ["rap", "trap"], "moods": ["sakin", "melankolik"], "activities": ["gece"], "language": "en", "year": 2019, "duration": "2:57", "bpm": 126, "cover_url": "", "spotify_url": "#none", "reason": "Travis Scott'in sakin sarkisi"},

    # Kanye West
    {"id": "s505", "name": "Power", "artist": "Kanye West", "album": "My Beautiful Dark Twisted Fantasy", "genres": ["rap", "elektronik"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "gym"], "language": "en", "year": 2010, "duration": "4:52", "bpm": 152, "cover_url": "", "spotify_url": "#none", "reason": "Kanye'nin guc sarkisi"},
    {"id": "s506", "name": "Runaway", "artist": "Kanye West", "album": "My Beautiful Dark Twisted Fantasy", "genres": ["rap", "rnb"], "moods": ["melankolik", "uzgun"], "activities": ["gece", "yagmur"], "language": "en", "year": 2010, "duration": "9:08", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": "Kanye'nin basyapidi"},
    {"id": "s507", "name": "All of the Lights", "artist": "Kanye West", "album": "My Beautiful Dark Twisted Fantasy", "genres": ["rap", "pop"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "spor"], "language": "en", "year": 2010, "duration": "4:59", "bpm": 127, "cover_url": "", "spotify_url": "#none", "reason": "Kanye'nin efsane sarkisi"},
    {"id": "s508", "name": "Gold Digger", "artist": "Kanye West", "album": "Late Registration", "genres": ["rap"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "en", "year": 2005, "duration": "3:12", "bpm": 106, "cover_url": "", "spotify_url": "#none", "reason": "Kanye'nin klasik sarkisi"},
    {"id": "s509", "name": "Love Lockdown", "artist": "Kanye West", "album": "808s & Heartbreak", "genres": ["rap", "elektronik"], "moods": ["uzgun", "melankolik"], "activities": ["gece"], "language": "en", "year": 2008, "duration": "4:31", "bpm": 138, "cover_url": "", "spotify_url": "#none", "reason": "Kanye'nin duygusal sarkisi"},

    # Duman
    {"id": "s510", "name": "Bu Akvam", "artist": "Duman", "album": "Duman I", "genres": ["turkce_rock"], "moods": ["enerjik", "sinirli"], "activities": ["araba", "spor"], "language": "tr", "year": 2009, "duration": "3:40", "bpm": 120, "cover_url": "", "spotify_url": "#none", "reason": "Duman'in sert sarkisi"},
    {"id": "s511", "name": "Oje", "artist": "Duman", "album": "Duman II", "genres": ["turkce_rock"], "moods": ["mutlu", "enerjik"], "activities": ["araba", "parti"], "language": "tr", "year": 2013, "duration": "3:25", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "Duman'in eglenceli sarkisi"},
    {"id": "s512", "name": "Kufuri", "artist": "Duman", "album": "Duman I", "genres": ["turkce_rock"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 2009, "duration": "4:00", "bpm": 90, "cover_url": "", "spotify_url": "#none", "reason": "Duman'in duygusal sarkisi"},
    {"id": "s513", "name": "Senden Daha Guzel", "artist": "Duman", "album": "Belki Alismam Lazim", "genres": ["turkce_rock"], "moods": ["romantik", "uzgun"], "activities": ["gece"], "language": "tr", "year": 2002, "duration": "4:30", "bpm": 85, "cover_url": "", "spotify_url": "#none", "reason": "Duman'in romantik sarkisi"},

    # Teoman
    {"id": "s515", "name": "Ruzgar Gulu", "artist": "Teoman", "album": "O", "genres": ["turkce_rock"], "moods": ["romantik", "sakin"], "activities": ["gece", "kahve"], "language": "tr", "year": 2000, "duration": "3:50", "bpm": 85, "cover_url": "", "spotify_url": "#none", "reason": "Teoman'in romantik sarkisi"},
    {"id": "s516", "name": "Paramparca", "artist": "Teoman", "album": "En Guzel Hikayem", "genres": ["turkce_rock"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 2004, "duration": "4:05", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Teoman'in duygusal sarkisi"},
    {"id": "s517", "name": "Ask Bir Yangin", "artist": "Teoman", "album": "Ask Bir Yangin", "genres": ["turkce_rock"], "moods": ["romantik", "enerjik"], "activities": ["araba"], "language": "tr", "year": 2006, "duration": "3:45", "bpm": 110, "cover_url": "", "spotify_url": "#none", "reason": "Teoman'in ask sarkisi"},
    {"id": "s518", "name": "Renkli Ruyalar Oteli", "artist": "Teoman", "album": "Renkli Ruyalar Oteli", "genres": ["turkce_rock"], "moods": ["sakin", "nostaljik"], "activities": ["gece", "kahve"], "language": "tr", "year": 2003, "duration": "4:20", "bpm": 75, "cover_url": "", "spotify_url": "#none", "reason": "Teoman'in nostaljik sarkisi"},

    # Ibrahim Tatlises
    {"id": "s520", "name": "Mavi Mavi", "artist": "Ibrahim Tatlises", "album": "Mavi Mavi", "genres": ["arabesk"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1985, "duration": "4:00", "bpm": 80, "cover_url": "", "spotify_url": "#none", "reason": "Ibrahim Tatlises'in klasiği"},
    {"id": "s521", "name": "Yanlizim", "artist": "Ibrahim Tatlises", "album": "Yanlizim", "genres": ["arabesk"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1990, "duration": "3:50", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Ibrahim Tatlises'in duygusal sarkisi"},
    {"id": "s522", "name": "Her Seyi Yak", "artist": "Ibrahim Tatlises", "album": "Her Seyi Yak", "genres": ["arabesk"], "moods": ["sinirli", "enerjik"], "activities": ["araba"], "language": "tr", "year": 1995, "duration": "3:40", "bpm": 110, "cover_url": "", "spotify_url": "#none", "reason": "Ibrahim Tatlises'in sert sarkisi"},
    {"id": "s523", "name": "Bir Gun Beni Ararsan", "artist": "Ibrahim Tatlises", "album": "Bir Gun Beni Ararsan", "genres": ["arabesk"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1998, "duration": "4:10", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Ibrahim Tatlises'in romantik sarkisi"},

    # Gulsen
    {"id": "s525", "name": "Lokomotif", "artist": "Gulsen", "album": "Yurtta Ask Cihanda Ask", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "tr", "year": 2003, "duration": "3:30", "bpm": 125, "cover_url": "", "spotify_url": "#none", "reason": "Gulsen'in eglenceli hiti"},
    {"id": "s526", "name": "Yatcaz Kalkcaz Ortak", "artist": "Gulsen", "album": "Yatcaz Kalkcaz Ortak", "genres": ["turkce_pop"], "moods": ["mutlu", "romantik"], "activities": ["parti"], "language": "tr", "year": 2015, "duration": "3:15", "bpm": 118, "cover_url": "", "spotify_url": "#none", "reason": "Gulsen'in populer sarkisi"},
    {"id": "s527", "name": "Bangir Bangir", "artist": "Gulsen", "album": "Bangir Bangir", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "tr", "year": 2011, "duration": "3:10", "bpm": 130, "cover_url": "", "spotify_url": "#none", "reason": "Gulsen'in dans sarkisi"},
    {"id": "s528", "name": "Bir Ihtimal Var", "artist": "Gulsen", "album": "Yapragizi", "genres": ["turkce_pop"], "moods": ["romantik", "uzgun"], "activities": ["gece"], "language": "tr", "year": 2009, "duration": "3:50", "bpm": 95, "cover_url": "", "spotify_url": "#none", "reason": "Gulsen'in duygusal sarkisi"},

    # Kenan Dogulu
    {"id": "s530", "name": "Cak Bir Selamet", "artist": "Kenan Dogulu", "album": "Kenan Dogulu", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti", "araba"], "language": "tr", "year": 2006, "duration": "3:30", "bpm": 130, "cover_url": "", "spotify_url": "#none", "reason": "Kenan Dogulu'nun parti sarkisi"},
    {"id": "s531", "name": "Oyle Bir Gecer Ki Zaman", "artist": "Kenan Dogulu", "album": "Kenan Dogulu", "genres": ["turkce_pop"], "moods": ["uzgun", "nostaljik"], "activities": ["gece"], "language": "tr", "year": 2007, "duration": "4:00", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Kenan Dogulu'nun duygusal sarkisi"},
    {"id": "s532", "name": "Uc Horoz", "artist": "Kenan Dogulu", "album": "Kenan Dogulu", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti"], "language": "tr", "year": 2008, "duration": "3:15", "bpm": 125, "cover_url": "", "spotify_url": "#none", "reason": "Kenan Dogulu'nun eglenceli sarkisi"},

    # Ceza
    {"id": "s534", "name": "Rapstar", "artist": "Ceza", "album": "Rapstar", "genres": ["turkce_rap"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "tr", "year": 2006, "duration": "3:40", "bpm": 95, "cover_url": "", "spotify_url": "#none", "reason": "Ceza'nin hit rap sarkisi"},
    {"id": "s535", "name": "Nem Kaldi", "artist": "Ceza", "album": "Rapstar", "genres": ["turkce_rap"], "moods": ["sinirli", "enerjik"], "activities": ["spor"], "language": "tr", "year": 2006, "duration": "3:30", "bpm": 90, "cover_url": "", "spotify_url": "#none", "reason": "Ceza'nin sert rap sarkisi"},
    {"id": "s536", "name": "Holocaust", "artist": "Ceza", "album": "Rapstar", "genres": ["turkce_rap"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "gym"], "language": "tr", "year": 2006, "duration": "3:50", "bpm": 98, "cover_url": "", "spotify_url": "#none", "reason": "Ceza'nin motivasyon sarkisi"},

    # Sagopa Kajmer
    {"id": "s538", "name": "Bir Istek Var", "artist": "Sagopa Kajmer", "album": "Bir Istek Var", "genres": ["turkce_rap"], "moods": ["melankolik", "uzgun"], "activities": ["gece", "yagmur"], "language": "tr", "year": 2007, "duration": "4:00", "bpm": 85, "cover_url": "", "spotify_url": "#none", "reason": "Sagopa Kajmer'in duygusal sarkisi"},
    {"id": "s539", "name": "Ateş Hattı", "artist": "Sagopa Kajmer", "album": "Kendine Gel", "genres": ["turkce_rap"], "moods": ["enerjik", "sinirli"], "activities": ["spor", "gym"], "language": "tr", "year": 2009, "duration": "3:40", "bpm": 92, "cover_url": "", "spotify_url": "#none", "reason": "Sagopa Kajmer'in sert sarkisi"},
    {"id": "s540", "name": "Alisten Koptum", "artist": "Sagopa Kajmer", "album": "Sagopa Kajmer", "genres": ["turkce_rap"], "moods": ["melankolik", "sakin"], "activities": ["gece"], "language": "tr", "year": 2003, "duration": "4:20", "bpm": 80, "cover_url": "", "spotify_url": "#none", "reason": "Sagopa Kajmer'in sakin rap sarkisi"},

    # Muslum Gurses
    {"id": "s542", "name": "Yorgunum", "artist": "Muslum Gurses", "album": "Muslum Gurses", "genres": ["arabesk", "damar"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1990, "duration": "4:00", "bpm": 82, "cover_url": "", "spotify_url": "#none", "reason": "Muslum Gurses'in duygusal sarkisi"},
    {"id": "s543", "name": "Yalan Dunya", "artist": "Muslum Gurses", "album": "Yalan Dunya", "genres": ["arabesk", "damar"], "moods": ["uzgun", "sinirli"], "activities": ["gece"], "language": "tr", "year": 1987, "duration": "3:45", "bpm": 85, "cover_url": "", "spotify_url": "#none", "reason": "Muslum Gurses'in asi sarkisi"},
    {"id": "s544", "name": "Bana Bir Seyler Anlat", "artist": "Muslum Gurses", "album": "Muslum Gurses", "genres": ["arabesk"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1992, "duration": "3:50", "bpm": 78, "cover_url": "", "spotify_url": "#none", "reason": "Muslum Gurses'in romantik sarkisi"},

    # Ferdi Tayfur
    {"id": "s546", "name": "Huzurlumusun", "artist": "Ferdi Tayfur", "album": "Huzurlumusun", "genres": ["arabesk", "fantazi"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "yagmur"], "language": "tr", "year": 1980, "duration": "4:00", "bpm": 76, "cover_url": "", "spotify_url": "#none", "reason": "Ferdi Tayfur'un duygusal sarkisi"},
    {"id": "s547", "name": "Dalinda O Kadin", "artist": "Ferdi Tayfur", "album": "Dalinda O Kadin", "genres": ["arabesk"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1990, "duration": "3:40", "bpm": 80, "cover_url": "", "spotify_url": "#none", "reason": "Ferdi Tayfur'un romantik sarkisi"},
    {"id": "s548", "name": "Yildizlar Benim Olsun", "artist": "Ferdi Tayfur", "album": "Yildizlar Benim Olsun", "genres": ["arabesk"], "moods": ["uzgun", "nostaljik"], "activities": ["yagmur"], "language": "tr", "year": 1985, "duration": "3:50", "bpm": 74, "cover_url": "", "spotify_url": "#none", "reason": "Ferdi Tayfur'un nostaljik sarkisi"},

    # Baris Manco
    {"id": "s550", "name": "Guzpece Günler", "artist": "Baris Manco", "album": "Baris Manco", "genres": ["anadolu_rock"], "moods": ["mutlu", "nostaljik"], "activities": ["araba", "yazlik"], "language": "tr", "year": 1975, "duration": "3:30", "bpm": 105, "cover_url": "", "spotify_url": "#none", "reason": "Baris Manco'nun mutlu sarkisi"},
    {"id": "s551", "name": "Iste Baris Iste Manco", "artist": "Baris Manco", "album": "Baris Manco", "genres": ["anadolu_rock"], "moods": ["enerjik", "mutlu"], "activities": ["parti", "araba"], "language": "tr", "year": 1976, "duration": "3:20", "bpm": 115, "cover_url": "", "spotify_url": "#none", "reason": "Baris Manco'nun enerjik sarkisi"},
    {"id": "s552", "name": "Canimin Ici", "artist": "Baris Manco", "album": "Yeni Bir Gun", "genres": ["anadolu_rock"], "moods": ["romantik", "mutlu"], "activities": ["araba"], "language": "tr", "year": 1978, "duration": "3:40", "bpm": 100, "cover_url": "", "spotify_url": "#none", "reason": "Baris Manco'nun romantik sarkisi"},

    # Sezen Aksu (ek)
    {"id": "s554", "name": "Kutlama", "artist": "Sezen Aksu", "album": "Gulumse", "genres": ["turkce_pop"], "moods": ["mutlu", "enerjik"], "activities": ["parti"], "language": "tr", "year": 1991, "duration": "3:30", "bpm": 115, "cover_url": "", "spotify_url": "#none", "reason": "Sezen Aksu'nun eglenceli sarkisi"},
    {"id": "s555", "name": "Ruhuma Asla", "artist": "Sezen Aksu", "album": "Gulumse", "genres": ["turkce_pop"], "moods": ["uzgun", "romantik"], "activities": ["gece"], "language": "tr", "year": 1991, "duration": "4:00", "bpm": 88, "cover_url": "", "spotify_url": "#none", "reason": "Sezen Aksu'nun romantik sarkisi"},

    # Imagine Dragons
    {"id": "s557", "name": "Believer", "artist": "Imagine Dragons", "album": "Evolve", "genres": ["rock", "pop"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "gym"], "language": "en", "year": 2017, "duration": "3:24", "bpm": 140, "cover_url": "", "spotify_url": "#none", "reason": "Imagine Dragons'in motivasyon sarkisi"},
    {"id": "s558", "name": "Thunder", "artist": "Imagine Dragons", "album": "Evolve", "genres": ["rock", "pop"], "moods": ["enerjik", "mutlu"], "activities": ["spor", "araba"], "language": "en", "year": 2017, "duration": "3:07", "bpm": 168, "cover_url": "", "spotify_url": "#none", "reason": "Imagine Dragons'in populer hiti"},
    {"id": "s559", "name": "Radioactive", "artist": "Imagine Dragons", "album": "Night Visions", "genres": ["rock", "alternatif_rock"], "moods": ["enerjik", "epik"], "activities": ["spor", "oyun"], "language": "en", "year": 2012, "duration": "3:06", "bpm": 136, "cover_url": "", "spotify_url": "#none", "reason": "Imagine Dragons'in efsane sarkisi"},
    {"id": "s560", "name": "Demons", "artist": "Imagine Dragons", "album": "Night Visions", "genres": ["rock", "pop"], "moods": ["melankolik", "uzgun"], "activities": ["gece", "yagmur"], "language": "en", "year": 2012, "duration": "2:57", "bpm": 142, "cover_url": "", "spotify_url": "#none", "reason": "Imagine Dragons'in duygusal sarkisi"},

    # Radiohead
    {"id": "s562", "name": "Karma Police", "artist": "Radiohead", "album": "OK Computer", "genres": ["alternatif_rock", "indie"], "moods": ["melankolik", "sinirli"], "activities": ["gece", "araba"], "language": "en", "year": 1997, "duration": "4:21", "bpm": 126, "cover_url": "", "spotify_url": "#none", "reason": "Radiohead'in ikonik sarkisi"},
    {"id": "s563", "name": "No Surprises", "artist": "Radiohead", "album": "OK Computer", "genres": ["alternatif_rock", "indie"], "moods": ["sakin", "melankolik"], "activities": ["gece", "yagmur"], "language": "en", "year": 1997, "duration": "3:48", "bpm": 84, "cover_url": "", "spotify_url": "#none", "reason": "Radiohead'in huzurlu sarkisi"},
    {"id": "s564", "name": "High and Dry", "artist": "Radiohead", "album": "The Bends", "genres": ["alternatif_rock"], "moods": ["uzgun", "melankolik"], "activities": ["gece", "araba"], "language": "en", "year": 1995, "duration": "4:17", "bpm": 126, "cover_url": "", "spotify_url": "#none", "reason": "Radiohead'in duygusal sarkisi"},
    {"id": "s565", "name": "Fake Plastic Trees", "artist": "Radiohead", "album": "The Bends", "genres": ["alternatif_rock"], "moods": ["melankolik", "sakin"], "activities": ["gece", "ders"], "language": "en", "year": 1995, "duration": "4:50", "bpm": 96, "cover_url": "", "spotify_url": "#none", "reason": "Radiohead'in sakin sarkisi"},

    # Daft Punk
    {"id": "s567", "name": "Harder Better Faster Stronger", "artist": "Daft Punk", "album": "Discovery", "genres": ["elektronik", "funk"], "moods": ["enerjik", "motivasyon"], "activities": ["spor", "gym"], "language": "en", "year": 2001, "duration": "3:45", "bpm": 142, "cover_url": "", "spotify_url": "#none", "reason": "Daft Punk'in motivasyon sarkisi"},
    {"id": "s568", "name": "Digital Love", "artist": "Daft Punk", "album": "Discovery", "genres": ["elektronik", "funk"], "moods": ["mutlu", "romantik"], "activities": ["parti", "araba"], "language": "en", "year": 2001, "duration": "4:58", "bpm": 128, "cover_url": "", "spotify_url": "#none", "reason": "Daft Punk'in romantik sarkisi"},
    {"id": "s569", "name": "Something About Us", "artist": "Daft Punk", "album": "Discovery", "genres": ["elektronik", "rnb"], "moods": ["romantik", "sakin"], "activities": ["gece", "kahve"], "language": "en", "year": 2001, "duration": "3:36", "bpm": 72, "cover_url": "", "spotify_url": "#none", "reason": "Daft Punk'in duygusal sarkisi"},
]