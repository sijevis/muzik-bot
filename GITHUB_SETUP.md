# GitHub'a Yükleme Kılavuzu

Bu dosya, projeyi GitHub'a güvenli şekilde yüklemek için adım adım talimatları içerir.

## ⚠️ Yüklemeden ÖNCE Kontrol Et

`.gitignore` dosyası aşağıdaki **hassas dosyaları** otomatik olarak engelleyecek:

- ✅ `backend/.env` (API anahtarları)
- ✅ `backend/firebase-credentials.json` (Firebase service account)
- ✅ `backend/muzikbot.db` (Veritabanı)
- ✅ `backend/*.log` (Log dosyaları)
- ✅ `frontend/.env` (Frontend env)
- ✅ `node_modules/`, `venv/` (Bağımlılıklar)

**Hiçbir API anahtarın repo'ya yüklenmeyecek.**

---

## Yöntem 1: GitHub Web Arayüzü ile (En Kolay)

### Adım 1: GitHub'da Yeni Repo Oluştur
1. https://github.com/new adresine git
2. Repository name: `muzik-bot` (veya `dj-ai`)
3. Description: `Türkçe doğal dil işleme ile müzik öneri asistanı`
4. **Public** seç
5. ⚠️ **README, .gitignore, license EKLEME** (zaten elimizde var)
6. "Create repository" tıkla

### Adım 2: Git Komutları (PowerShell'de çalıştır)

```powershell
cd D:\muzik-bot

# Git başlat
git init

# Tüm dosyaları ekle (.gitignore otomatik filtreleyecek)
git add .

# İlk commit
git commit -m "Initial commit: DJ AI - Türkçe müzik öneri asistanı"

# Ana branch'i main yap
git branch -M main

# GitHub repo'yu remote olarak ekle (YUKARIDA OLUSTURDUGUN REPO URL)
git remote add origin https://github.com/<KULLANICI-ADIN>/muzik-bot.git

# Push et
git push -u origin main
```

İlk push'ta GitHub kullanıcı adı ve şifre/token isteyecek. **Şifre yerine Personal Access Token kullan:**
- https://github.com/settings/tokens
- "Generate new token (classic)" → repo izinleri seç → kopyala

---

## Yöntem 2: GitHub Desktop ile (GUI)

1. https://desktop.github.com/ adresinden indir
2. GitHub hesabınla giriş yap
3. "File > Add Local Repository" → `D:\muzik-bot` seç
4. "Create a repository" → name: `muzik-bot`
5. "Publish repository" → Public seç → Publish

---

## Yöntem 3: VS Code ile

1. VS Code'da `D:\muzik-bot` klasörünü aç
2. Sol menüden "Source Control" (Ctrl+Shift+G)
3. "Initialize Repository" tıkla
4. Mesaj yaz: "Initial commit"
5. Commit (Ctrl+Enter)
6. "Publish to GitHub" → Public seç

---

## Yükleme Sonrası

### Repo Ayarları (Önerilen)
1. Repo > Settings > General:
   - About kısmına açıklama ve topic ekle:
     - Topics: `python`, `flask`, `react`, `nlp`, `turkish`, `spotify`, `chatbot`, `music`

2. Repo > Settings > Pages (opsiyonel):
   - Frontend'i GitHub Pages ile yayınla

### README'ye Demo Eklenmesi (İsteğe Bağlı)
- Ekran görüntüleri al (`screenshots/` klasörüne koy)
- README.md'ye `![Screenshot](screenshots/demo.png)` ekle

---

## Sorun Giderme

### "Repository not found" hatası
```powershell
git remote -v  # Mevcut remote'u gör
git remote set-url origin https://github.com/<DOGRU-KULLANICI>/muzik-bot.git
```

### "Permission denied" hatası
- Personal Access Token oluştur ve şifre yerine kullan
- Veya SSH key kullan: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### Yanlışlıkla .env push ettiysen
```powershell
# Repo'dan çıkar (lokal'de kalır)
git rm --cached backend/.env
git commit -m "Remove sensitive .env file"
git push

# ÖNEMLİ: API anahtarlarını HEMEN yenile (eski anahtarlar artık güvensiz)
```

---

## Hızlı Komutlar Özeti

```powershell
cd D:\muzik-bot
git init
git add .
git status                                          # Neler eklenecek kontrol et
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USER/REPO.git
git push -u origin main
```

İyi şanslar! 🚀
