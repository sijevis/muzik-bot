# 🎵 DJ AI - Yapay Zeka Destekli Müzik Öneri Asistanı

> Türkçe doğal dil işleme ile çalışan, kişiselleştirilmiş müzik öneri ve playlist oluşturma sistemi

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18.2-61DAFB.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000.svg)](https://flask.palletsprojects.com/)
[![Spotify API](https://img.shields.io/badge/Spotify-API-1DB954.svg)](https://developer.spotify.com/)

## 📖 Proje Hakkında

DJ AI, kullanıcıların doğal dilde (özellikle Türkçe) yazdığı mesajları analiz ederek müzik türü, ruh hali, aktivite ve sanatçı tercihlerini tespit eden ve kişiselleştirilmiş şarkı önerileri sunan bir yapay zeka asistanıdır. Sistem, sohbet arayüzü üzerinden kullanıcılarla etkileşim kurar, akıllı playlist'ler oluşturur ve bunları doğrudan Spotify hesabına aktarma imkanı sağlar.

### ✨ Temel Özellikler

- 🤖 **Türkçe Doğal Dil İşleme**: Türkçe dilbilgisi eklerini (-de, -e, -i, vb.) tanıyan akıllı analiz motoru
- 🎯 **Niyet Tespiti**: Tür, ruh hali, aktivite, sanatçı bazlı sınıflandırma (%97.5 doğruluk)
- 📋 **Akıllı Playlist Oluşturma**: Kullanıcının tercihlerine göre dinamik playlist üretimi
- 🎼 **Geniş Müzik Veritabanı**: 278 şarkı, 96 sanatçı, 40+ tür
- 🌐 **Spotify Entegrasyonu**: OAuth ile hesap bağlama ve playlist aktarımı
- 🔐 **Firebase Authentication**: Kullanıcı kayıt/giriş sistemi
- 💾 **Kalıcı Veri**: SQLite veya Firestore ile playlist/tercih kaydetme
- 🌙 **Karanlık/Aydınlık Tema**: Modern, responsive React arayüzü
- ⚡ **LLM Desteği**: OpenAI ve Google Gemini entegrasyonu (opsiyonel)
- 🎨 **Demo Modu**: API anahtarı olmadan tam fonksiyonel çalışma

## 🏗️ Mimari

```
┌─────────────────────┐     ┌─────────────────────┐     ┌──────────────────┐
│   React Frontend    │────▶│   Flask Backend     │────▶│  Spotify API     │
│   (Port 3000)       │     │   (Port 5000)       │     │  Firebase        │
│                     │     │                     │     │  OpenAI/Gemini   │
│  - Chat UI          │     │  - NLP Analyzer     │     └──────────────────┘
│  - Playlist View    │     │  - Playlist Gen.    │
│  - Spotify Connect  │     │  - Memory Store     │
└─────────────────────┘     └─────────────────────┘
                                       │
                                       ▼
                            ┌──────────────────────┐
                            │  SQLite / Firestore  │
                            └──────────────────────┘
```

## 🛠️ Teknoloji Yığını

### Backend
- **Python 3.9+** - Programlama dili
- **Flask 3.0** - Web framework
- **SQLite / Firebase Firestore** - Veritabanı
- **Spotipy** - Spotify Web API client
- **Firebase Admin** - Kimlik doğrulama
- **OpenAI / Google Gemini** - LLM entegrasyonu (opsiyonel)

### Frontend
- **React 18** - UI framework
- **Tailwind CSS** - Stil
- **Framer Motion** - Animasyonlar
- **Axios** - HTTP client
- **Firebase JS SDK** - Kimlik doğrulama

## 🚀 Kurulum

### Gereksinimler
- Python 3.9 veya üzeri
- Node.js 16 veya üzeri
- npm

### 1. Projeyi Klonla
```bash
git clone https://github.com/<kullanici-adin>/muzik-bot.git
cd muzik-bot
```

### 2. Backend Kurulumu
```bash
cd backend

# Virtual environment oluştur
python -m venv venv

# Aktive et (Windows)
venv\Scripts\activate

# Aktive et (Linux/Mac)
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# .env dosyasını oluştur
cp .env.example .env
# .env dosyasını düzenleyerek API anahtarlarını ekle (opsiyonel - demo modu için gerekli değil)
```

### 3. Frontend Kurulumu
```bash
cd ../frontend

# Bağımlılıkları yükle
npm install

# .env dosyasını oluştur (opsiyonel - Firebase için)
cp .env.example .env
```

### 4. Çalıştırma

**Backend** (terminal 1):
```bash
cd backend
python app.py
# http://localhost:5000
```

**Frontend** (terminal 2):
```bash
cd frontend
npm start
# http://localhost:3000
```

## 🔑 API Anahtarları (Opsiyonel)

Tam fonksiyonalite için aşağıdaki servislerden API anahtarı alabilirsiniz. **Demo modunda hiçbiri gerekli değildir.**

| Servis | Kullanım | Link |
|--------|----------|------|
| Spotify | Gerçek şarkı verisi ve playlist aktarımı | [developer.spotify.com](https://developer.spotify.com/dashboard) |
| OpenAI | Gelişmiş LLM yanıtları | [platform.openai.com](https://platform.openai.com/api-keys) |
| Google Gemini | Alternatif LLM | [aistudio.google.com](https://aistudio.google.com/app/apikey) |
| Firebase | Kullanıcı kimlik doğrulama | [console.firebase.google.com](https://console.firebase.google.com) |

### 🔒 Güvenlik Notu

> **`.env` dosyaları ve API anahtarları güvenlik gerekçesiyle bu repoya dahil edilmemiştir.**
>
> Projeyi çalıştırmak için aşağıdaki adımları izleyin:
>
> 1. `backend/.env.example` dosyasını `backend/.env` olarak kopyalayın
> 2. `frontend/.env.example` dosyasını `frontend/.env` olarak kopyalayın
> 3. Kendi API anahtarlarınızı bu dosyalara ekleyin
> 4. Firebase için: `firebase-credentials.json` dosyanızı `backend/` klasörüne koyun
>
> ⚠️ **API anahtarlarınızı asla `.env` dosyasının dışında bir yere yazmayın ve commit etmeyin.** `.gitignore` dosyası bu hassas dosyaları otomatik olarak engeller.
>
> 💡 API anahtarı olmadan da uygulama **Demo Modu**'nda tam fonksiyonel çalışır (278 şarkılık yerel veri seti ile).

## 📊 Performans Metrikleri

| Metrik | Değer |
|--------|-------|
| Intent Classification Doğruluğu | **%97.5** |
| Türkçe Ek İşleme Doğruluğu | **%86.7** |
| Şarkı Önerisi Alaka Düzeyi | **%100** (ortalama) |
| API Başarı Oranı | **%100** |
| Veri Seti | 278 şarkı, 96 sanatçı, 40 tür |

Detaylı rapor için: [`reports/REPORT.md`](reports/REPORT.md)

## 📁 Proje Yapısı

```
muzik-bot/
├── backend/
│   ├── app.py                  # Flask API
│   ├── analyzer.py             # Türkçe NLP analiz motoru
│   ├── playlist.py             # Playlist üretici
│   ├── music_service.py        # Spotify/Demo müzik servisi
│   ├── llm_service.py          # OpenAI/Gemini entegrasyonu
│   ├── memory.py               # SQLite/Firestore veri katmanı
│   ├── demo_data.py            # 278 şarkılık veri seti
│   ├── firebase_config.py      # Firebase yapılandırması
│   ├── generate_report.py      # Rapor üretici
│   ├── test_e2e.py             # End-to-end testler
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/         # React bileşenleri
│   │   ├── context/            # React Context (Auth, Theme)
│   │   ├── services/           # API ve Firebase servisleri
│   │   └── App.js
│   ├── public/
│   └── package.json
│
├── reports/                    # Otomatik üretilen raporlar
│   ├── figures/                # Grafikler (PNG)
│   ├── tables/                 # Tablolar (CSV)
│   ├── REPORT.md
│   └── metrics.json
│
├── .gitignore
└── README.md
```

## 🧪 Test ve Rapor

### E2E Testleri Çalıştır
```bash
cd backend
python test_e2e.py
```

### Otomatik Rapor Oluştur
```bash
cd backend
python generate_report.py
# Çıktı: ../reports/ klasöründe 9 grafik, 5 CSV, REPORT.md
```

## 🎯 Kullanım Örnekleri

Kullanıcı, sohbet arayüzüne aşağıdaki gibi mesajlar yazabilir:

- 💬 *"Bana rock müzik öner"*
- 💬 *"Spor yaparken dinleyeceğim şarkılar"*
- 💬 *"Üzgünüm, ne dinleyebilirim?"*
- 💬 *"Tarkan dinlemek istiyorum"*
- 💬 *"10 şarkılık lo-fi playlist yap"*
- 💬 *"Yağmurlu havada motivasyona ihtiyacım var"*

Sistem mesajı analiz ederek tercihlerinizi tespit eder ve uygun öneriler sunar.

## 🤝 Katkıda Bulunma

Katkılarınız memnuniyetle karşılanır! Lütfen:

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'e push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request açın

## 📝 Lisans

Bu proje akademik amaçlar için geliştirilmiştir.

## 👤 Geliştirici

**Baran**

---

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!
