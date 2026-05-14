#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate DJ AI project documentation PDF using fpdf2 with built-in Unicode support."""

from fpdf import FPDF
import os

TURKISH_ASCII_MAP = {
    "\u0131": "i", "\u0130": "I",
    "ö": "o", "Ö": "O",
    "ü": "u", "Ü": "U",
    "ş": "s", "Ş": "S",
    "ç": "c", "Ç": "C",
    "ğ": "g", "Ğ": "G",
}

def tr(text):
    for k, v in TURKISH_ASCII_MAP.items():
        text = text.replace(k, v)
    return text

class DJAI_PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        # Use fpdf2's built-in Helvetica which supports basic chars
        # For Turkish chars, we'll use unicode mode

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, tr("DJ AI v2.1 - Proje Dokumantasyonu"), align="R")
            self.ln(4)
            self.set_draw_color(200, 200, 200)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, tr(f"Sayfa {self.page_no()}/{{nb}}"), align="C")

    def section_title(self, num, title):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(30, 64, 120)
        self.cell(0, 12, tr(f"{num}. {title}"), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(30, 64, 120)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def subsection_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(50, 90, 150)
        self.cell(0, 10, tr(title), new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, tr(text))
        self.ln(2)

    def bold_text(self, text):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, tr(text))
        self.ln(1)

    def code_block(self, code):
        self.set_font("Courier", "", 8)
        self.set_text_color(50, 50, 50)
        self.set_fill_color(245, 245, 245)
        lines = code.strip().split("\n")
        for line in lines:
            self.cell(0, 5, tr(f"  {line}"), new_x="LMARGIN", new_y="NEXT", fill=True)
        self.ln(3)

    def bullet_point(self, text, indent=10):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        x = self.get_x()
        self.set_x(x + indent)
        self.cell(5, 6, ">")
        self.multi_cell(0, 6, tr(text))
        self.ln(1)

    def table_row(self, cells, widths, bold=False, fill=False):
        if bold:
            self.set_font("Helvetica", "B", 9)
        else:
            self.set_font("Helvetica", "", 9)
        if fill:
            self.set_fill_color(230, 240, 255)
        self.set_text_color(40, 40, 40)
        for i, (cell, width) in enumerate(zip(cells, widths)):
            self.cell(width, 7, tr(str(cell)), border=1, fill=fill, new_x="RIGHT", new_y="TOP")
        self.ln()

    def info_box(self, text):
        self.set_fill_color(230, 245, 255)
        self.set_draw_color(100, 160, 220)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 60, 120)
        y = self.get_y()
        self.rect(10, y, 190, 12, style="DF")
        self.set_xy(12, y + 2)
        self.multi_cell(186, 5, tr(text))
        self.set_y(y + 14)


def generate_pdf():
    pdf = DJAI_PDF()
    pdf.alias_nb_pages()

    # ===== COVER PAGE =====
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font("Helvetica", "B", 32)
    pdf.set_text_color(30, 64, 120)
    pdf.cell(0, 15, "DJ AI v2.1", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Yapay Zeka Destekli Turkce Muzik Oneri Chatbot'u", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_draw_color(30, 64, 120)
    pdf.line(50, pdf.get_y(), 160, pdf.get_y())
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Proje Dokumantasyonu & Teknik Analiz", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.cell(0, 8, "Flask + React | Python | JavaScript | SQLite | Spotify API | OpenAI/Gemini", align="C", new_x="LMARGIN", new_y="NEXT")

    # ===== TABLE OF CONTENTS =====
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(30, 64, 120)
    pdf.cell(0, 12, "Icindekiler", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    toc = [
        ("1", "Proje Ozeti & Amac"),
        ("2", "Sistem Mimarisi"),
        ("3", "Backend - Flask API (app.py)"),
        ("4", "NLP & Sohbet Motoru (analyzer.py)"),
        ("5", "LLM Entegrasyonu (llm_service.py)"),
        ("6", "Veritabani & Hafiza (memory.py)"),
        ("7", "Playlist Sistemi (playlist.py)"),
        ("8", "Demo Veritabani (demo_data.py)"),
        ("9", "Muzik Servisi (music_service.py)"),
        ("10", "Frontend - React Uygulamasi"),
        ("11", "Kimlik Dogrulama Sistemi"),
        ("12", "Veri Akisi - Sohbet Mesaji Yasam Dongusu"),
        ("13", "Sohbet Asama Sistemi (Conversation Stage)"),
        ("14", "Baglam Koruma & Duzeltme Sistemi"),
        ("15", "API Endpoint'leri"),
        ("16", "Kurulum & Calistirma"),
    ]
    for num, title in toc:
        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(40, 40, 40)
        pdf.cell(0, 7, f"  {num}.  {title}", new_x="LMARGIN", new_y="NEXT")

    # ===== 1 =====
    pdf.add_page()
    pdf.section_title("1", "Proje Ozeti & Amac")
    pdf.body_text(
        "DJ AI, yapay zeka destekli, Turkce konusan bir muzik oneri chatbot'udur. "
        "Kullanicilara dogal dilde sohbet ederek ruh halini, aktivitesini ve muzik tercihlerini anlar, "
        "bu bilgilere dayali olarak kisisellestirilmis muzik onnerileri sunar."
    )
    pdf.subsection_title("Temel Ozellikler")
    pdf.bullet_point("Turkce dogal dil anlama - 30+ tur, 12 ruh hali, 17 aktivite, 70+ sanatci anahtar kelime veritabani")
    pdf.bullet_point("3 asamali sohbet akisi - Ruh hali sorgulama > Aktivite sorgulama > Oneri sunma")
    pdf.bullet_point("Baglam koruma - Duzeltme, tur degisikligi, reddetme durumlarinda onceki baglami korur")
    pdf.bullet_point("Coklu LLM destegi - OpenAI GPT, Google Gemini, yerel Ollama ile sirali yedekleme")
    pdf.bullet_point("Spotify entegrasyonu - Sarki zenginlestirme, playlist disa aktarma")
    pdf.bullet_point("278 demo sarki - API anahtari olmadan da calisir")
    pdf.bullet_point("Kullanici kimlik dogrulama - Firebase + e-posta/sifre + misafir modu")
    pdf.bullet_point("Playlist olusturma - Tercih bazli akilli puanlama sistemi")

    pdf.subsection_title("Teknoloji Yigini")
    pdf.table_row(["Katman", "Teknoloji", "Amac"], [35, 55, 100], bold=True, fill=True)
    pdf.table_row(["Backend", "Flask (Python 3.13)", "REST API sunucusu"], [35, 55, 100])
    pdf.table_row(["Veritabani", "SQLite + Firebase Firestore", "Kullanici, sohbet, tercih verileri"], [35, 55, 100])
    pdf.table_row(["AI", "OpenAI / Gemini / Ollama", "Dogal dil yanitlama"], [35, 55, 100])
    pdf.table_row(["Muzik", "Spotify Web API (spotipy)", "Canli sarki arama & zenginlestirme"], [35, 55, 100])
    pdf.table_row(["Frontend", "React 18 + Tailwind CSS", "Kullanici arayuzu"], [35, 55, 100])
    pdf.table_row(["Auth", "Firebase Auth + SQLite", "Kimlik dogrulama"], [35, 55, 100])
    pdf.table_row(["NL", "Ozel NLP (analyzer.py)", "Turkce anahtar kelime eslestirme"], [35, 55, 100])

    # ===== 2 =====
    pdf.add_page()
    pdf.section_title("2", "Sistem Mimarisi")
    pdf.body_text(
        "DJ AI, uc katmanli bir mimari kullanir: React frontend, Flask backend API ve veri katmani. "
        "Frontend, backend ile REST API uzerinden haberlesir. Backend, NLP motoru, LLM servisleri, "
        "Spotify API'si ve veritabani arasinda kopru gorevi gorur."
    )
    pdf.subsection_title("Mimari Diyagram")
    pdf.code_block(
        "+-----------------+     +------------------------------------+\n"
        "| React Frontend  |---->|      Flask Backend (app.py)        |\n"
        "| localhost:3000  |     |  +-----------+  +---------------+  |\n"
        "|  AuthPage.js    |     |  | analyzer  |  | llm_service   |  |\n"
        "|  ChatArea.js    |     |  | .py       |  | .py           |  |\n"
        "|  Sidebar.js     |     |  +-----------+  +---------------+  |\n"
        "|  PlaylistView   |     |  +-----------+  +---------------+  |\n"
        "+-----------------+     |  | playlist  |  | music_service |  |\n"
        "                        |  | .py       |  | .py           |  |\n"
        "                        |  +-----------+  +---------------+  |\n"
        "                        |  +-----------+  +---------------+  |\n"
        "                        |  | memory    |  | firebase      |  |\n"
        "                        |  | .py       |  | _config.py    |  |\n"
        "                        |  +-----------+  +---------------+  |\n"
        "                        +------------------------------------+\n"
        "                               |          |          |\n"
        "                          +----+     +----+     +----+\n"
        "                          v          v          v\n"
        "                     SQLite DB   Spotify API  OpenAI/Gemini"
    )

    # ===== 3 =====
    pdf.add_page()
    pdf.section_title("3", "Backend - Flask API (app.py)")
    pdf.body_text(
        "app.py, DJ AI'in ana sunucu dosyasidir. Flask ile 15+ REST API endpoint tanimlar, "
        "rate limiting uygular, oturum durumu yonetir ve tum servisleri bir araya getirir."
    )
    pdf.subsection_title("Sohbet Akisi (chat endpoint)")
    pdf.code_block(
        "POST /api/chat\n"
        "  1. Kullanici mesajini al\n"
        "  2. Mesaji analiz et (tur, ruh hali, aktivite)\n"
        "  3. Oturum durumunu getir (conversation_stage)\n"
        "  4. LLM yaniti dene (OpenAI > Gemini > Ollama)\n"
        "  5. LLM yoksa ResponseGenerator ile demo yanit uret\n"
        "  6. Oturum durumunu guncelle ve kaydet\n"
        "  7. Yaniti JSON olarak dondur"
    )
    pdf.subsection_title("Oturum Durumu Yonetimi")
    pdf.body_text(
        "Her sohbet oturumu (session_id + user_id ile anahtarlanmis) bir asama ve baglam objesi tutar. "
        "Bu sayede bot, kullanicinin onceki ruh halini ve aktivitesini hatirlar."
    )
    pdf.code_block(
        'conversation_states = {\n'
        '    "user_id:session_id": {\n'
        '        "stage": "asking_mood|asking_activity|recommending",\n'
        '        "context": {\n'
        '            "mood": "uzgun|mutlu|enerjik|...",\n'
        '            "genre": "rock|pop|rap|...",\n'
        '            "activity": "ders|spor|gece|...",\n'
        '            ...\n'
        '        }\n'
        '    }\n'
        '}'
    )

    # ===== 4 =====
    pdf.add_page()
    pdf.section_title("4", "NLP & Sohbet Motoru (analyzer.py)")
    pdf.body_text(
        "analyzer.py, DJ AI'in kalbidir. Iki ana sinif icerir: "
        "MessageAnalyzer (anahtar kelime tespiti) ve ResponseGenerator (asama tabanli yanit uretimi)."
    )
    pdf.subsection_title("MessageAnalyzer - Anahtar Kelime Tespiti")
    pdf.body_text(
        "Kullanici mesajini Turkce karakter normalizasyonu ile isler. "
        "Ardindan 4 kategoride bulanik eslestirme (fuzzy matching) yapar:"
    )
    pdf.bullet_point("Tur tespiti - 30+ tur (rock, pop, rap, jazz, klasik, lofi, arabesk, anadolu_rock...)")
    pdf.bullet_point("Ruh hali tespiti - 12 duygu (mutlu, uzgun, enerjik, romantik, asik, sakin, motivasyon, sinirli, melankolik, nostaljik, guclu, epik)")
    pdf.bullet_point("Aktivite tespiti - 17 aktivite (ders, spor, gece, yolculuk, uyku, parti, kahve, yagmur, araba, kosu, oyun, kod, chill, odak, meditasyon...)")
    pdf.bullet_point("Sanatci tespiti - 50+ sanatci (Queen, Tarkan, Sezen Aksu, Duman, Pink Floyd...)")

    pdf.subsection_title("Turkce Karakter Normalizasyonu")
    pdf.code_block(
        'TURKISH_REPLACEMENTS = {\n'
        '    "c": "c", "g": "g", "i": "i", "o": "o",\n'
        '    "s": "s", "u": "u", "I": "I", "C": "C",\n'
        '    "G": "G", "O": "O", "S": "S", "U": "U"\n'
        '}'
    )
    pdf.body_text(
        "Bu sayede kullanici Turkce eklerle yazdiginda (ornegin \"iyiyim\", \"mutluyum\", \"uzgunum\") "
        "anahtar kelimeler dogru eslestirilir."
    )

    pdf.subsection_title("ResponseGenerator - Asama Tabanli Yanit Sistemi")
    pdf.table_row(["Asama", "Aciklama", "Gecis Kosulu"], [35, 90, 65], bold=True, fill=True)
    pdf.table_row(["asking_mood", "Bot ruh halini sorar", "Ruh hali algilandiginda > asking_activity"], [35, 90, 65])
    pdf.table_row(["asking_activity", "Bot ne yaptigini sorar", "Aktivite algilandiginda > recommending"], [35, 90, 65])
    pdf.table_row(["recommending", "Muzik onnerisi sunar", "Duzeltme/tur degisikliginde kalir"], [35, 90, 65])

    pdf.subsection_title("Duzeltme & Baglam Koruma")
    pdf.bullet_point("Tur degisikligi - \"rap olsun\", \"rock degil\" > yeni tur, mood/activity korunur")
    pdf.bullet_point("Reddetme - \"olmadi\", \"istemem\" > alternatif oneri sunar")
    pdf.bullet_point("Devam - \"tamam\", \"evet\" > sohbeti surdurur")
    pdf.bullet_point("Daha fazla - \"daha\", \"baska\" > ayni baglamda yeni oneri sunar")

    # ===== 5 =====
    pdf.add_page()
    pdf.section_title("5", "LLM Entegrasyonu (llm_service.py)")
    pdf.body_text(
        "LLMClient, uc farkli AI saglayicisini sirali yedekleme (fallback) zinciri ile kullanir. "
        "Bir saglayici basarisiz olursa veya yanit vermezse, bir sonraki saglayici denenir."
    )
    pdf.subsection_title("Yedekleme Zinciri")
    pdf.code_block(
        "OpenAI (GPT-3.5/4) > Gemini (2.0-flash) > Ollama (llama3) > Demo Modu\n"
        "      basarisiz           basarisiz          basarisiz"
    )
    pdf.subsection_title("Sistem Prompt'u")
    pdf.body_text(
        "LLM'ler, Turkce konusan sicak ve dogal bir muzik asistani olarak yonlendirilir. "
        "Ana kurallar: Robot gibi konusma, sarki ismi uydurma, once anlamaya calis."
    )
    pdf.subsection_title("Streaming Destegi")
    pdf.body_text(
        "OpenAI icin streaming modu mevcuttur (/api/chat/stream endpoint'i). "
        "Yanitlar token token gonderilir, kullanici uzun yanitlari beklemeden gorebilir."
    )

    # ===== 6 =====
    pdf.add_page()
    pdf.section_title("6", "Veritabani & Hafiza (memory.py)")
    pdf.body_text(
        "MemoryStore sinifi, cift katmanli veri saklama saglar: SQLite (varsayilan) ve Firebase Firestore (istege bagli)."
    )
    pdf.subsection_title("Veritabani Tablolari")
    pdf.table_row(["Tablo", "Amac", "Anahtar Alanlar"], [40, 70, 80], bold=True, fill=True)
    pdf.table_row(["users", "Kullanici bilgileri", "user_id (PK), display_name"], [40, 70, 80])
    pdf.table_row(["accounts", "E-posta/sifre girisi", "user_id (PK), email (UQ), password_hash"], [40, 70, 80])
    pdf.table_row(["preferences", "Kullanici tercihleri", "user_id, category, value"], [40, 70, 80])
    pdf.table_row(["conversations", "Sohbet gecmisi", "user_id, session_id, role, content, analysis"], [40, 70, 80])
    pdf.table_row(["playlists", "Olusturulan playlistler", "id, user_id, name, preferences"], [40, 70, 80])
    pdf.table_row(["playlist_songs", "Playlist sarkilari", "playlist_id, song_name, artist, genre"], [40, 70, 80])

    # ===== 7 =====
    pdf.add_page()
    pdf.section_title("7", "Playlist Sistemi (playlist.py)")
    pdf.body_text(
        "PlaylistGenerator, kullanici tercihlerine gore demo veritabanindan sarkilari puanlayarak "
        "kisisellestirilmis playlistler olusturur."
    )
    pdf.table_row(["Kriter", "Puan", "Aciklama"], [50, 25, 115], bold=True, fill=True)
    pdf.table_row(["Tur eslesmesi", "+3/tur", "Secilen turlere uygun sarkilar"], [50, 25, 115])
    pdf.table_row(["Ruh hali eslesmesi", "+2", "Secilen ruh haline uygun sarkilar"], [50, 25, 115])
    pdf.table_row(["Aktivite eslesmesi", "+2", "Secilen aktiviteye uygun sarkilar"], [50, 25, 115])
    pdf.table_row(["Sanatci eslesmesi", "+5", "Tam sanatci eslesmesi"], [50, 25, 115])
    pdf.table_row(["Dil eslesmesi", "+1", "Turkce/Ingilizce tercihi eslesmesi"], [50, 25, 115])
    pdf.table_row(["Sevilmeyen tur", "-5", "Kullanicinin sevmedigi turlerde cezalandirma"], [50, 25, 115])

    # ===== 8 =====
    pdf.add_page()
    pdf.section_title("8", "Demo Veritabani (demo_data.py)")
    pdf.body_text(
        "API anahtari olmadan da uygulamanin calisabilmesi icin 278 demo sarki tanimlanmistir. "
        "Her sarki su metadata'ya sahiptir: name, artist, album, genres[], moods[], activities[], "
        "language, cover_url, spotify_url, duration, reason."
    )
    pdf.bullet_point("278 sarki - Turkce ve Ingilizce")
    pdf.bullet_point("30+ tur kategorisi (rock, pop, rap, jazz, klasik, lofi, arabesk, anadolu_rock...)")
    pdf.bullet_point("12 ruh hali etiketi")
    pdf.bullet_point("17 aktivite etiketi")
    pdf.bullet_point("Spotify URL'leri (mevcut olan sarkilar icin)")

    # ===== 9 =====
    pdf.add_page()
    pdf.section_title("9", "Muzik Servisi (music_service.py)")
    pdf.body_text(
        "MusicClient, iki katmanli bir mimari sunar: SpotifyService (canli API) ve DemoMusicService (yedek). "
        "Spotify erisimi varsa canli arama ve onneriler yapilir, yoksa demo veritabani kullanilir."
    )
    pdf.bullet_point("spotipy kutuphanesi ile Spotify Web API'ye erisim")
    pdf.bullet_point("Sarki arama (search_tracks) - sanatci veya genel arama")
    pdf.bullet_point("Oneri alma (get_recommendations) - tur bazli onneriler")
    pdf.bullet_point("Sarki zenginlestirme (enrich_songs) - demo sarkilarina kapak resmi ve Spotify link ekleme")
    pdf.bullet_point("Otomatik token yenileme - suresi dolan access_token'lari refresh_token ile yeniler")

    # ===== 10 =====
    pdf.add_page()
    pdf.section_title("10", "Frontend - React Uygulamasi")
    pdf.body_text("DJ AI'in frontend'i React 18 ve Tailwind CSS ile olusturulmustur.")
    pdf.subsection_title("Bilesen Hiyerarşisi")
    pdf.code_block(
        "index.js\n"
        "  +-- AuthProvider (context)\n"
        "  +-- ThemeProvider (context)\n"
        "       +-- App.js (ana durum yonetimi)\n"
        "            |-- [giris yapilmadi] > AuthPage\n"
        "            |    +-- Giris formu (e-posta/sifre + Google SSO)\n"
        "            |    +-- Kayit formu\n"
        "            |    +-- Ucretsiz Dene (misafir modu)\n"
        "            |\n"
        "            +-- [giris yapildi] > Ana duzen\n"
        "                 +-- Sidebar (kategoriler, playlistler, sanatcilar)\n"
        "                 +-- ChatArea (mesaj listesi + girdi)\n"
        "                 +-- PlaylistView (olusturulan playlist)\n"
        "                 +-- SharePlaylistModal (kaydetme/paylasma)"
    )
    pdf.subsection_title("Ozellikler")
    pdf.bullet_point("Karanlik/aydinlik tema destegi (localStorage ile kalici)")
    pdf.bullet_point("Yanit yaziyor animasyonu (TypingIndicator)")
    pdf.bullet_point("Sarki mini kartlari (kapak resmi, sanatci, tur etiketi)")
    pdf.bullet_point("Kategori butonlari ile hizli mesaj gonderme")
    pdf.bullet_point("Responsive tasarim (mobil uyumlu)")

    # ===== 11 =====
    pdf.add_page()
    pdf.section_title("11", "Kimlik Dogrulama Sistemi")
    pdf.body_text("Uc farkli giris yontemi desteklenir. Firebase yapilandirilmamissa sistem SQLite tabanli e-posta/sifre ile calisir.")
    pdf.table_row(["Yontem", "Mekanizma", "Veri Saklama"], [40, 70, 80], bold=True, fill=True)
    pdf.table_row(["Google SSO", "Firebase Auth popup", "Firebase + SQLite senkron"], [40, 70, 80])
    pdf.table_row(["E-posta/Sifre", "Backend hash dogrulama", "SQLite accounts tablosu"], [40, 70, 80])
    pdf.table_row(["Misafir", "UUID olusturma", "localStorage (sunucu kaydi yok)"], [40, 70, 80])

    pdf.subsection_title("Sifre Guvenligi")
    pdf.bullet_point("PBKDF2-HMAC-SHA256 ile tuzlananmis (salted) hash - 100.000 iterasyon")
    pdf.bullet_point("Eski SHA256 hash destegi (geriye donuk uyumluluk)")
    pdf.bullet_point("Firebase ID token dogrulama (Google SSO icin)")

    # ===== 12 =====
    pdf.add_page()
    pdf.section_title("12", "Veri Akisi - Sohbet Mesaji Yasam Dongusu")
    pdf.body_text("Bir kullanicinin mesaj gondermesinden yaniti gormesine kadar olan adimlar:")
    pdf.bullet_point("Adim 1: Kullanici ChatArea'ya mesaj yazar ve gonderir")
    pdf.bullet_point("Adim 2: Frontend POST /api/chat istegi yapar (message, session_id, user_id)")
    pdf.bullet_point("Adim 3: Backend mesaji memory'ye kaydeder (save_message)")
    pdf.bullet_point("Adim 4: MessageAnalyzer ile mesaji analiz eder (tur, ruh hali, aktivite tespiti)")
    pdf.bullet_point("Adim 5: Oturum durumunu getirir (conversation_states dict'inden)")
    pdf.bullet_point("Adim 6: Playlist istegi mi kontrol eder (is_playlist_request)")
    pdf.bullet_point("Adim 7: Playlist istegi varsa > PlaylistGenerator ile playlist olusturur")
    pdf.bullet_point("Adim 8: Playlist istegi yoksa > ResponseGenerator ile yanit uretir (asama tabanli)")
    pdf.bullet_point("Adim 9: LLM modu aktifse > once LLM yaniti denenir (OpenAI > Gemini > Ollama)")
    pdf.bullet_point("Adim 10: LLM basarisizsa > Spotify API denenir (sarki arama/oneri)")
    pdf.bullet_point("Adim 11: Spotify da yoksa > Demo veritabanindan sarki secilir")
    pdf.bullet_point("Adim 12: Yanit ve sarkilar JSON olarak frontend'e dondurulur")
    pdf.bullet_point("Adim 13: Frontend mesaji chat listesine ekler, sarki kartlarini gosterir")

    # ===== 13 =====
    pdf.add_page()
    pdf.section_title("13", "Sohbet Asama Sistemi (Conversation Stage)")
    pdf.body_text("Bot, her mesajda konusmanin hangi asamasinda oldugunu takip eder. Bu sayede aceleci yanit vermek yerine once kullaniciyi anlar.")
    pdf.subsection_title("Asama Diyagrami")
    pdf.code_block(
        "                    +------------------+\n"
        "     Kullanici ---->|   asking_mood    |<-- Yeni sohbet baslangici\n"
        "     girisi       |  (Ruh hali sor)   |\n"
        "                    +--------+---------+\n"
        "                             | Ruh hali algilandi\n"
        "                             v\n"
        "                    +------------------+\n"
        "                    | asking_activity  |\n"
        "                    | (Aktivite sor)   |\n"
        "                    +--------+---------+\n"
        "                             | Aktivite algilandi\n"
        "                             v\n"
        "                    +------------------+\n"
        "    Duzeltme ---->|  recommending    |<-- Tur degisikliginde kalir\n"
        "    Tur degisikligi|  (Oneri sun)     |\n"
        "    Reddetme       +------------------+"
    )
    pdf.subsection_title("Ornek Sohbet Akisi")
    pdf.info_box("Kullanici: Merhaba > Bot: Selamlar! Ruh halin nasil bugun? (asking_mood)")
    pdf.info_box("Kullanici: Uzgunum > Bot: Anladim... Peki ne yapiyorsun? (asking_activity)")
    pdf.info_box("Kullanici: Ders calisiyorum > Bot: Oneriler: 1. Breathe 2. Yesterday 3. Comfortably Numb (recommending)")
    pdf.info_box("Kullanici: Bunlar rock degil, rap olsun > Bot: Haklisin, duzeltiyorum (recommending, baglam korunur)")

    # ===== 14 =====
    pdf.add_page()
    pdf.section_title("14", "Baglam Koruma & Duzeltme Sistemi")
    pdf.body_text("Bot, oneri sonrasi kullanicinin duzeltme, reddetme veya tur degisikligie yapmasieden onceki baglamin basina sarmas.")
    pdf.subsection_title("Duzeltme Algialama")
    pdf.table_row(["Kullanici Derse", "Algilama", "Bot Tepkisi"], [70, 35, 85], bold=True, fill=True)
    pdf.table_row(["\"Bunlar rock degil\"", "Tur duzeltme", "Yeni turde oneri, mood/activity korunur"], [70, 35, 85])
    pdf.table_row(["\"Rap olsun\"", "Tur degisikligi", "Yeni turde oneri"], [70, 35, 85])
    pdf.table_row(["\"Olmadi, begenmedim\"", "Reddetme", "Alternatif oneri"], [70, 35, 85])
    pdf.table_row(["\"Daha fazla oner\"", "Devam", "Ayni baglamda yeni oneri"], [70, 35, 85])
    pdf.table_row(["\"Tamam, evet\"", "Kabul", "Sohbeti surdurur"], [70, 35, 85])
    pdf.table_row(["\"Turkce olsun\"", "Dil degisikligi", "Turkce filtre ile oneri"], [70, 35, 85])

    # ===== 15 =====
    pdf.add_page()
    pdf.section_title("15", "API Endpoint'leri")
    pdf.body_text("DJ AI backend'i 20+ REST API endpoint sunar:")
    pdf.subsection_title("Sohbet & Oneri")
    pdf.table_row(["Endpoint", "Method", "Aciklama"], [70, 20, 100], bold=True, fill=True)
    pdf.table_row(["/api/chat", "POST", "Ana sohbet endpoint'i"], [70, 20, 100])
    pdf.table_row(["/api/chat/stream", "POST", "Streaming sohbet (SSE)"], [70, 20, 100])
    pdf.table_row(["/api/categories", "GET", "Kategori listesi"], [70, 20, 100])
    pdf.table_row(["/api/artists", "GET", "Sanatci listesi"], [70, 20, 100])
    pdf.table_row(["/api/status", "GET", "Sistem durumu"], [70, 20, 100])

    pdf.subsection_title("Kimlik Dogrulama")
    pdf.table_row(["/api/auth/register", "POST", "E-posta/sifre ile kayit"], [70, 20, 100])
    pdf.table_row(["/api/auth/login", "POST", "E-posta/sifre ile giris"], [70, 20, 100])
    pdf.table_row(["/api/auth/verify", "POST", "Firebase token dogrulama"], [70, 20, 100])
    pdf.table_row(["/api/auth/status", "GET", "Firebase yapilandirma durumu"], [70, 20, 100])
    pdf.table_row(["/api/auth/spotify-link", "POST", "Spotify hesabi baglama"], [70, 20, 100])
    pdf.table_row(["/api/auth/spotify-unlink", "POST", "Spotify baglantisini kaldirma"], [70, 20, 100])

    pdf.subsection_title("Kullanici & Playlist")
    pdf.table_row(["/api/user/:id/preferences", "GET", "Kullanici tercihleri"], [70, 20, 100])
    pdf.table_row(["/api/user/:id/playlists", "GET", "Kullanici playlistleri"], [70, 20, 100])
    pdf.table_row(["/api/playlist/:id", "GET", "Tekil playlist detayi"], [70, 20, 100])
    pdf.table_row(["/api/playlist/:id/rename", "POST", "Playlist isim degisikligi"], [70, 20, 100])
    pdf.table_row(["/api/playlist/:id/delete", "POST", "Playlist silme"], [70, 20, 100])
    pdf.table_row(["/api/playlist/suggest-name", "POST", "AI playlist isim onerisi"], [70, 20, 100])
    pdf.table_row(["/api/reset/:session", "POST", "Oturumu sifirlama"], [70, 20, 100])
    pdf.table_row(["/api/spotify/export-playlist", "POST", "Spotify'a playlist disa aktarma"], [70, 20, 100])

    # ===== 16 =====
    pdf.add_page()
    pdf.section_title("16", "Kurulum & Calistirma")
    pdf.subsection_title("Gereksinimler")
    pdf.bullet_point("Python 3.10+")
    pdf.bullet_point("Node.js 16+")
    pdf.bullet_point("Spotify API anahtari (istege bagli)")
    pdf.bullet_point("OpenAI veya Gemini API anahtari (istege bagli)")

    pdf.subsection_title("Backend Kurulumu")
    pdf.code_block(
        "cd backend\n"
        "pip install -r requirements.txt\n"
        "cp .env.example .env      # API anahtarlarini guncelle\n"
        "python app.py              # Gelistirme modu\n"
        "python run_production.py    # Uretim modu (Waitress)"
    )
    pdf.subsection_title("Frontend Kurulumu")
    pdf.code_block(
        "cd frontend\n"
        "npm install\n"
        "npm start                  # Gelistirme modu (localhost:3000)\n"
        "npm run build              # Uretim derlemesi"
    )
    pdf.subsection_title("Demo Modu")
    pdf.body_text(
        "API anahtarlari olmadan uygulama demo modunda calisir. Bu modda: "
        "LLM yanitlari kullanilmaz, ResponseGenerator demo yanitlar uretir; "
        "Spotify API cagrilari yapilmaz, 278 demo sarki kullanilir; "
        "Firebase kimlik dogrulama kullanilmaz, e-posta/sifre ve misafir modu calisir."
    )

    # Save
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DJ AI_Dokumantasyon.pdf")
    pdf.output(output_path)
    print(f"PDF olusturuldu: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_pdf()