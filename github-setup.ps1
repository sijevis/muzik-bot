Set-Location 'D:\muzik-bot'

Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  DJ AI Projesi - GitHub Yukleme" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Mevcut dizin: $(Get-Location)" -ForegroundColor Gray
Write-Host ""
Write-Host "ADIM 1: GitHub'da yeni repo olustur" -ForegroundColor Yellow
Write-Host "        https://github.com/new" -ForegroundColor White
Write-Host "        Name: muzik-bot (veya dj-ai)" -ForegroundColor White
Write-Host "        Public sec, README/gitignore EKLEME" -ForegroundColor White
Write-Host ""
Write-Host "ADIM 2: Asagidaki komutlari sirayla calistir:" -ForegroundColor Yellow
Write-Host ""
Write-Host "   git init" -ForegroundColor Green
Write-Host "   git add ." -ForegroundColor Green
Write-Host "   git status" -ForegroundColor Green
Write-Host "   git commit -m `"Initial commit: DJ AI - Turkce muzik oneri asistani`"" -ForegroundColor Green
Write-Host "   git branch -M main" -ForegroundColor Green
Write-Host "   git remote add origin https://github.com/KULLANICI-ADIN/muzik-bot.git" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host ""
Write-Host "NOT: Push'ta sifre yerine Personal Access Token kullan:" -ForegroundColor Magenta
Write-Host "     https://github.com/settings/tokens" -ForegroundColor White
Write-Host ""
Write-Host "Detayli kilavuz: D:\muzik-bot\GITHUB_SETUP.md" -ForegroundColor Gray
Write-Host ""
