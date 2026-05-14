"""
DJ AI - Otomatik Rapor Olusturma Sistemi
==========================================
Bu script, projenin tum metriklerini olcer ve rapor icin grafikler/tablolar uretir.

Cikti:
- reports/figures/*.png    -> Grafikler
- reports/tables/*.csv     -> Tablolar
- reports/metrics.json     -> Tum metrikler JSON
- reports/REPORT.md        -> Markdown rapor
"""

import sys
import os
import json
import time
import io
from collections import Counter, defaultdict
from datetime import datetime

# UTF-8 cikti
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Proje modulleri
from analyzer import MessageAnalyzer, ResponseGenerator
from demo_data import DEMO_SONGS, GENRE_LABELS, MOOD_LABELS, ACTIVITY_LABELS
from playlist import PlaylistGenerator
from music_service import MusicClient

# Stil
sns.set_style("whitegrid")
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 100
plt.rcParams["savefig.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"

REPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
FIG_DIR = os.path.join(REPORT_DIR, "figures")
TAB_DIR = os.path.join(REPORT_DIR, "tables")
os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(TAB_DIR, exist_ok=True)

# Renk paleti
COLORS = {
    "primary": "#8b5cf6",
    "secondary": "#06b6d4",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "spotify": "#1DB954",
}
PALETTE = ["#8b5cf6", "#06b6d4", "#10b981", "#f59e0b", "#ef4444", "#1DB954", "#ec4899", "#3b82f6"]

metrics = {}

print("=" * 70)
print("DJ AI - RAPOR OLUSTURMA SISTEMI")
print("=" * 70)
print(f"Cikti dizini: {REPORT_DIR}")
print()


# =====================================================================
# 1. DATASET STATISTICS
# =====================================================================
print("[1/6] Dataset istatistikleri analiz ediliyor...")

dataset_metrics = {
    "total_songs": len(DEMO_SONGS),
    "total_genres": len(GENRE_LABELS),
    "total_moods": len(MOOD_LABELS),
    "total_activities": len(ACTIVITY_LABELS),
}

# Tur dagilimi
genre_counter = Counter()
for s in DEMO_SONGS:
    for g in s.get("genres", []):
        genre_counter[g] += 1

# Dil dagilimi
lang_counter = Counter(s.get("language", "unknown") for s in DEMO_SONGS)

# Mood dagilimi
mood_counter = Counter()
for s in DEMO_SONGS:
    for m in s.get("moods", []):
        mood_counter[m] += 1

# Activity dagilimi
activity_counter = Counter()
for s in DEMO_SONGS:
    for a in s.get("activities", []):
        activity_counter[a] += 1

# Yil dagilimi
year_counter = Counter()
for s in DEMO_SONGS:
    year = s.get("year")
    if year:
        decade = (year // 10) * 10
        year_counter[decade] += 1

# Unique artists
artist_counter = Counter(s.get("artist", "") for s in DEMO_SONGS)
unique_artists = len([a for a in artist_counter if a])

dataset_metrics.update({
    "unique_artists": unique_artists,
    "top_10_genres": dict(genre_counter.most_common(10)),
    "language_distribution": dict(lang_counter),
    "top_10_moods": dict(mood_counter.most_common(10)),
    "top_10_activities": dict(activity_counter.most_common(10)),
    "decade_distribution": dict(sorted(year_counter.items())),
    "top_10_artists": dict(artist_counter.most_common(10)),
})
metrics["dataset"] = dataset_metrics

# --- GRAFIK 1: Tur Dagilimi (Top 15) ---
fig, ax = plt.subplots(figsize=(11, 6))
top_genres = genre_counter.most_common(15)
genres, counts = zip(*top_genres)
labels = [GENRE_LABELS.get(g, g) for g in genres]
bars = ax.barh(range(len(labels)), counts, color=PALETTE * 3)
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel("Sarki Sayisi", fontsize=11)
ax.set_title("Sekil 1: Veri Setindeki En Yaygin 15 Muzik Turu", fontsize=13, fontweight="bold", pad=15)
for i, (bar, count) in enumerate(zip(bars, counts)):
    ax.text(count + 1, i, str(count), va="center", fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig1_genre_distribution.png"))
plt.close()

# --- GRAFIK 2: Dil Dagilimi (Pasta) ---
fig, ax = plt.subplots(figsize=(8, 7))
lang_names = {"tr": "Turkce", "en": "Ingilizce", "unknown": "Diger"}
labels = [lang_names.get(k, k) for k in lang_counter.keys()]
values = list(lang_counter.values())
colors = [COLORS["primary"], COLORS["secondary"], COLORS["warning"]]
wedges, texts, autotexts = ax.pie(
    values, labels=labels, autopct=lambda p: f"{p:.1f}%\n({int(p*sum(values)/100)} sarki)",
    colors=colors[:len(values)], startangle=90, textprops={"fontsize": 11}
)
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontweight("bold")
ax.set_title("Sekil 2: Veri Setinin Dil Dagilimi", fontsize=13, fontweight="bold", pad=15)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig2_language_pie.png"))
plt.close()

# --- GRAFIK 3: Decade Dagilimi ---
fig, ax = plt.subplots(figsize=(10, 5))
decades = sorted(year_counter.keys())
counts = [year_counter[d] for d in decades]
ax.bar([f"{d}s" for d in decades], counts, color=COLORS["primary"], edgecolor="white", linewidth=2)
ax.set_xlabel("Donemi", fontsize=11)
ax.set_ylabel("Sarki Sayisi", fontsize=11)
ax.set_title("Sekil 3: Veri Setinin Donemler Bazinda Dagilimi", fontsize=13, fontweight="bold", pad=15)
for i, count in enumerate(counts):
    ax.text(i, count + 1, str(count), ha="center", fontsize=10, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig3_decade_distribution.png"))
plt.close()

# --- GRAFIK 4: Mood ve Activity Dagilimi (Yan yana) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
# Mood
top_moods = mood_counter.most_common(10)
moods, m_counts = zip(*top_moods)
ax1.barh(range(len(moods)), m_counts, color=COLORS["primary"])
ax1.set_yticks(range(len(moods)))
ax1.set_yticklabels([MOOD_LABELS.get(m, m) for m in moods])
ax1.invert_yaxis()
ax1.set_xlabel("Sarki Sayisi")
ax1.set_title("Sekil 4a: En Yaygin 10 Ruh Hali", fontweight="bold")
# Activity
top_acts = activity_counter.most_common(10)
acts, a_counts = zip(*top_acts)
ax2.barh(range(len(acts)), a_counts, color=COLORS["secondary"])
ax2.set_yticks(range(len(acts)))
ax2.set_yticklabels([ACTIVITY_LABELS.get(a, a) for a in acts])
ax2.invert_yaxis()
ax2.set_xlabel("Sarki Sayisi")
ax2.set_title("Sekil 4b: En Yaygin 10 Aktivite", fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig4_mood_activity.png"))
plt.close()

# CSV: dataset_summary
df_dataset = pd.DataFrame([
    ["Toplam Sarki", dataset_metrics["total_songs"]],
    ["Unique Sanatci", dataset_metrics["unique_artists"]],
    ["Toplam Tur", dataset_metrics["total_genres"]],
    ["Toplam Ruh Hali", dataset_metrics["total_moods"]],
    ["Toplam Aktivite", dataset_metrics["total_activities"]],
    ["Turkce Sarki", lang_counter.get("tr", 0)],
    ["Ingilizce Sarki", lang_counter.get("en", 0)],
], columns=["Metrik", "Deger"])
df_dataset.to_csv(os.path.join(TAB_DIR, "table1_dataset_summary.csv"), index=False, encoding="utf-8-sig")

print(f"  OK: {dataset_metrics['total_songs']} sarki, {unique_artists} sanatci, {len(genre_counter)} tur")


# =====================================================================
# 2. INTENT CLASSIFICATION ACCURACY
# =====================================================================
print("[2/6] Intent classification dogruluk testi...")

analyzer = MessageAnalyzer()
generator = ResponseGenerator(songs_db=DEMO_SONGS)

# Genisletilmis test seti
test_cases = [
    # Genre tests
    ("Rock muzik oner", "genre", "rock"),
    ("Pop sarki dinlemek istiyorum", "genre", "pop"),
    ("Rap muzik onerin", "genre", "rap"),
    ("Jazz parcalari ac", "genre", "jazz"),
    ("Klasik muzik istiyorum", "genre", "klasik"),
    ("Metal muzik onerin", "genre", "metal"),
    ("Elektronik muzik ac", "genre", "elektronik"),
    ("Lo-fi muzik istiyorum", "genre", "lofi"),
    ("Arabesk sarkilar oner", "genre", "arabesk"),
    ("Turkce pop oner", "genre", "turkce_pop"),
    ("Turkce rap dinleyecegim", "genre", "turkce_rap"),
    ("Indie muzik istiyorum", "genre", "indie"),
    ("Blues muzigi oner", "genre", "blues"),
    ("Funk sarki istiyorum", "genre", "funk"),
    ("R&B oner", "genre", "rnb"),
    # Mood tests
    ("Uzgunum", "mood", "uzgun"),
    ("Mutluyum bugun", "mood", "mutlu"),
    ("Enerjik hissediyorum", "mood", "enerjik"),
    ("Sakinlesmek istiyorum", "mood", "sakin"),
    ("Romantik bir sarki", "mood", "romantik"),
    ("Motivasyona ihtiyacim var", "mood", "motivasyon"),
    ("Moralim bozuk", "mood", "uzgun"),
    ("Cok mutluyum", "mood", "mutlu"),
    # Activity tests
    ("Spor yaparken dinleyecegim", "activity", "spor"),
    ("Derse calisirken muzik", "activity", "ders"),
    ("Gece yolculugu icin", "activity", "gece"),
    ("Yagmurlu havada", "activity", "yagmur"),
    ("Yolculuk muzigi", "activity", "yolculuk"),
    ("Parti muzigi oner", "activity", "parti"),
    ("Uyku oncesi muzik", "activity", "uyku"),
    # Artist tests
    ("Tarkan dinlemek istiyorum", "artist_present", True),
    ("Baris Manco sarkilari", "artist_present", True),
    ("Sezen Aksu oner", "artist_present", True),
    ("Queen dinleyecegim", "artist_present", True),
    # Greeting tests
    ("Merhaba", "greeting", True),
    ("Selam", "greeting", True),
    ("Naber", "greeting", True),
    # Playlist tests
    ("Bana playlist yap", "playlist_request", True),
    ("10 sarkilik liste yap", "playlist_request", True),
    ("Karisik playlist olustur", "playlist_request", True),
]

intent_results = {
    "genre": {"pass": 0, "fail": 0, "tests": []},
    "mood": {"pass": 0, "fail": 0, "tests": []},
    "activity": {"pass": 0, "fail": 0, "tests": []},
    "artist": {"pass": 0, "fail": 0, "tests": []},
    "greeting": {"pass": 0, "fail": 0, "tests": []},
    "playlist": {"pass": 0, "fail": 0, "tests": []},
}

# Confusion matrix data
true_intents = []
pred_intents = []

INTENT_TYPES = ["genre", "mood", "activity", "artist", "greeting", "playlist"]

def get_predicted_intent(analysis, msg):
    if analysis.get("is_playlist_request"):
        return "playlist"
    if analysis.get("genre"):
        return "genre"
    if analysis.get("mood"):
        return "mood"
    if analysis.get("activity"):
        return "activity"
    if analysis.get("artist"):
        return "artist"
    if analysis.get("confidence", 0) <= 0.2:
        return "greeting"
    return "unknown"

for msg, check_type, expected in test_cases:
    result = analyzer.analyze(msg)
    pred = get_predicted_intent(result, msg)
    
    # True intent
    if check_type == "artist_present":
        true_intent = "artist"
    elif check_type == "greeting":
        true_intent = "greeting"
    elif check_type == "playlist_request":
        true_intent = "playlist"
    else:
        true_intent = check_type
    
    true_intents.append(true_intent)
    pred_intents.append(pred)
    
    # Pass/Fail
    passed = False
    if check_type == "genre":
        passed = result.get("genre") == expected
    elif check_type == "mood":
        passed = result.get("mood") == expected
    elif check_type == "activity":
        passed = result.get("activity") == expected
    elif check_type == "artist_present":
        passed = bool(result.get("artist"))
    elif check_type == "greeting":
        passed = result.get("confidence", 0) <= 0.2
    elif check_type == "playlist_request":
        passed = bool(result.get("is_playlist_request"))
    
    category_key = check_type.replace("_present", "").replace("_request", "")
    if category_key in intent_results:
        if passed:
            intent_results[category_key]["pass"] += 1
        else:
            intent_results[category_key]["fail"] += 1
        intent_results[category_key]["tests"].append({"msg": msg, "expected": expected, "passed": passed})

# Accuracy
total_pass = sum(v["pass"] for v in intent_results.values())
total_fail = sum(v["fail"] for v in intent_results.values())
overall_accuracy = total_pass / (total_pass + total_fail) * 100

metrics["intent_classification"] = {
    "overall_accuracy": round(overall_accuracy, 2),
    "total_pass": total_pass,
    "total_fail": total_fail,
    "by_category": {k: {
        "pass": v["pass"],
        "fail": v["fail"],
        "accuracy": round(v["pass"] / (v["pass"] + v["fail"]) * 100, 2) if (v["pass"] + v["fail"]) > 0 else 0
    } for k, v in intent_results.items()}
}

# --- GRAFIK 5: Intent Accuracy per Category ---
fig, ax = plt.subplots(figsize=(10, 6))
categories = list(intent_results.keys())
accuracies = [intent_results[c]["pass"] / (intent_results[c]["pass"] + intent_results[c]["fail"]) * 100 if (intent_results[c]["pass"] + intent_results[c]["fail"]) > 0 else 0 for c in categories]
labels_tr = {"genre": "Tur", "mood": "Ruh Hali", "activity": "Aktivite", "artist": "Sanatci", "greeting": "Selamlama", "playlist": "Playlist"}
display_labels = [labels_tr.get(c, c) for c in categories]
colors_acc = [COLORS["success"] if a >= 90 else COLORS["warning"] if a >= 70 else COLORS["danger"] for a in accuracies]
bars = ax.bar(display_labels, accuracies, color=colors_acc, edgecolor="white", linewidth=2)
ax.set_ylabel("Dogruluk (%)", fontsize=11)
ax.set_title("Sekil 5: Niyet Sinifi (Intent) Dogruluk Oranlari", fontsize=13, fontweight="bold", pad=15)
ax.set_ylim(0, 110)
ax.axhline(y=overall_accuracy, color=COLORS["primary"], linestyle="--", linewidth=2, label=f"Genel Dogruluk: %{overall_accuracy:.1f}")
for bar, acc in zip(bars, accuracies):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f"%{acc:.1f}", ha="center", fontweight="bold")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig5_intent_accuracy.png"))
plt.close()

# --- GRAFIK 6: Confusion Matrix ---
all_intents = sorted(set(true_intents) | set(pred_intents))
cm = pd.crosstab(pd.Series(true_intents, name="Gercek"), pd.Series(pred_intents, name="Tahmin"))
# Ensure all intents present
for i in all_intents:
    if i not in cm.index:
        cm.loc[i] = 0
    if i not in cm.columns:
        cm[i] = 0
cm = cm.reindex(all_intents)[all_intents]

fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(cm, annot=True, fmt="d", cmap="Purples", ax=ax, cbar_kws={"label": "Test Sayisi"}, linewidths=0.5)
ax.set_title("Sekil 6: Intent Classification Confusion Matrix", fontsize=13, fontweight="bold", pad=15)
ax.set_xlabel("Tahmin Edilen Niyet", fontsize=11)
ax.set_ylabel("Gercek Niyet", fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig6_confusion_matrix.png"))
plt.close()

# CSV: intent accuracy
df_intent = pd.DataFrame([
    [labels_tr.get(c, c), intent_results[c]["pass"], intent_results[c]["fail"], 
     round(intent_results[c]["pass"] / (intent_results[c]["pass"] + intent_results[c]["fail"]) * 100, 2) if (intent_results[c]["pass"] + intent_results[c]["fail"]) > 0 else 0]
    for c in categories
], columns=["Kategori", "Basarili", "Basarisiz", "Dogruluk (%)"])
df_intent.to_csv(os.path.join(TAB_DIR, "table2_intent_accuracy.csv"), index=False, encoding="utf-8-sig")

print(f"  OK: Genel dogruluk %{overall_accuracy:.1f} ({total_pass}/{total_pass+total_fail})")


# =====================================================================
# 3. TURKISH SUFFIX HANDLING
# =====================================================================
print("[3/6] Turkce ek isleme testleri...")

suffix_tests = [
    ("Derse calisiyorum", "activity", "ders"),
    ("Spora gidecegim", "activity", "spor"),
    ("Uykum gelmiyor", "activity", "uyku"),
    ("Yolda gidiyorum", "activity", "yolculuk"),
    ("Mutluyum bugun", "mood", "mutlu"),
    ("Uzgunum arkadasim", "mood", "uzgun"),
    ("Enerjik hissediyorum", "mood", "enerjik"),
    ("Sakinlesmek istiyorum", "mood", "sakin"),
    ("Geceye selam", "activity", "gece"),
    ("Yagmurda yuruyorum", "activity", "yagmur"),
    ("Rocku severim", "genre", "rock"),
    ("Popu dinlerim", "genre", "pop"),
    ("Romantik hissediyorum", "mood", "romantik"),
    ("Motivasyona ihtiyacim var", "mood", "motivasyon"),
    ("Calisirken dinleyecegim", "activity", "ders"),
]

suffix_pass = 0
suffix_fail = 0
suffix_details = []
for msg, check_type, expected in suffix_tests:
    result = analyzer.analyze(msg)
    actual = result.get(check_type)
    passed = actual == expected
    if passed:
        suffix_pass += 1
    else:
        suffix_fail += 1
    suffix_details.append({"msg": msg, "type": check_type, "expected": expected, "actual": actual, "passed": passed})

suffix_accuracy = suffix_pass / (suffix_pass + suffix_fail) * 100
metrics["turkish_suffix"] = {
    "accuracy": round(suffix_accuracy, 2),
    "pass": suffix_pass,
    "fail": suffix_fail,
    "total_tests": len(suffix_tests),
}

df_suffix = pd.DataFrame(suffix_details)
df_suffix.columns = ["Mesaj", "Tip", "Beklenen", "Tahmin", "Basarili"]
df_suffix["Basarili"] = df_suffix["Basarili"].map({True: "EVET", False: "HAYIR"})
df_suffix.to_csv(os.path.join(TAB_DIR, "table3_turkish_suffix_tests.csv"), index=False, encoding="utf-8-sig")

print(f"  OK: %{suffix_accuracy:.1f} ({suffix_pass}/{len(suffix_tests)})")


# =====================================================================
# 4. SONG RELEVANCE (Genre-based)
# =====================================================================
print("[4/6] Sarki onerisi alaka duzeyi testleri...")

genre_relevance_tests = [
    ("rock", ["rock", "indie", "alternatif_rock", "grunge", "metal", "punk"]),
    ("pop", ["pop", "turkce_pop"]),
    ("rap", ["rap", "hiphop", "trap", "turkce_rap"]),
    ("lofi", ["lofi", "ambient", "neoklasik"]),
    ("arabesk", ["arabesk", "damar", "fantazi"]),
    ("jazz", ["jazz", "blues", "soul"]),
    ("klasik", ["klasik", "neoklasik"]),
    ("metal", ["metal", "rock", "punk"]),
    ("elektronik", ["elektronik", "edm", "house", "techno", "synthpop"]),
    ("turkce_pop", ["turkce_pop", "pop"]),
    ("turkce_rap", ["turkce_rap", "rap", "hiphop", "trap"]),
    ("indie", ["indie", "alternatif_rock", "rock"]),
]

relevance_results = []
for genre, related_genres in genre_relevance_tests:
    analysis = {"genre": genre, "genres": [genre], "mood": None, "activity": None,
                "artist": None, "language": None, "is_playlist_request": True,
                "playlist_count": 10, "confidence": 0.5, "keywords": [f"tur:{genre}"]}
    response = generator.generate_response(f"{genre} muzik oner", analysis)
    songs = response.get("songs", [])
    relevant = 0
    for s in songs:
        song_genres = s.get("genres", [s.get("genre", "")])
        if not isinstance(song_genres, list):
            song_genres = [song_genres]
        if any(rg in sg for rg in related_genres for sg in song_genres):
            relevant += 1
    pct = (relevant / len(songs) * 100) if songs else 0
    relevance_results.append({
        "Tur": GENRE_LABELS.get(genre, genre),
        "Onerilen": len(songs),
        "Alakali": relevant,
        "Alaka (%)": round(pct, 1)
    })

df_relevance = pd.DataFrame(relevance_results)
df_relevance.to_csv(os.path.join(TAB_DIR, "table4_song_relevance.csv"), index=False, encoding="utf-8-sig")

avg_relevance = df_relevance["Alaka (%)"].mean()
metrics["song_relevance"] = {
    "average_relevance": round(avg_relevance, 2),
    "by_genre": relevance_results,
}

# --- GRAFIK 7: Genre Relevance ---
fig, ax = plt.subplots(figsize=(12, 6))
genres_plot = df_relevance["Tur"].tolist()
relevances = df_relevance["Alaka (%)"].tolist()
colors_rel = [COLORS["success"] if r >= 70 else COLORS["warning"] if r >= 50 else COLORS["danger"] for r in relevances]
bars = ax.bar(range(len(genres_plot)), relevances, color=colors_rel, edgecolor="white", linewidth=2)
ax.set_xticks(range(len(genres_plot)))
ax.set_xticklabels(genres_plot, rotation=35, ha="right")
ax.set_ylabel("Alaka Duzeyi (%)", fontsize=11)
ax.set_title(f"Sekil 7: Tur Bazli Sarki Onerisi Alaka Duzeyi (Ortalama: %{avg_relevance:.1f})", fontsize=13, fontweight="bold", pad=15)
ax.set_ylim(0, 110)
ax.axhline(y=avg_relevance, color=COLORS["primary"], linestyle="--", linewidth=2, label=f"Ortalama: %{avg_relevance:.1f}")
ax.axhline(y=70, color=COLORS["success"], linestyle=":", linewidth=1.5, alpha=0.5, label="Iyi Esik: %70")
for bar, rel in zip(bars, relevances):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f"%{rel:.0f}", ha="center", fontweight="bold")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig7_genre_relevance.png"))
plt.close()

print(f"  OK: Ortalama alaka duzeyi %{avg_relevance:.1f}")


# =====================================================================
# 5. PERFORMANS (API Response Times)
# =====================================================================
print("[5/6] Performans olcumleri (API yanit sureleri)...")

API_URL = "http://localhost:5000"
performance_results = []

try:
    import requests
    
    test_messages = [
        "Rock muzik oner",
        "Turkce pop dinleyecegim",
        "Mutluyum",
        "Spor yaparken dinleyecegim",
        "Bana 5 sarkilik playlist yap",
        "Lo-fi muzik istiyorum",
        "Arabesk sarkilar oner",
        "Sakinlesmek istiyorum",
    ]
    
    response_times = []
    successful = 0
    failed = 0
    
    for msg in test_messages:
        try:
            t0 = time.time()
            r = requests.post(f"{API_URL}/api/chat", json={
                "message": msg,
                "session_id": f"perf_test_{int(t0)}",
                "user_id": "perf_test_user"
            }, timeout=30)
            elapsed = (time.time() - t0) * 1000  # ms
            response_times.append(elapsed)
            if r.status_code == 200:
                successful += 1
            else:
                failed += 1
            performance_results.append({"endpoint": "/api/chat", "message": msg, "time_ms": round(elapsed, 2), "status": r.status_code})
        except Exception as e:
            failed += 1
            performance_results.append({"endpoint": "/api/chat", "message": msg, "time_ms": -1, "status": "ERROR"})
    
    # Diger endpointleri test et
    other_endpoints = [
        ("/api/categories", "GET"),
        ("/api/status", "GET"),
        ("/api/artists", "GET"),
    ]
    for endpoint, method in other_endpoints:
        try:
            t0 = time.time()
            if method == "GET":
                r = requests.get(f"{API_URL}{endpoint}", timeout=10)
            elapsed = (time.time() - t0) * 1000
            performance_results.append({"endpoint": endpoint, "message": "-", "time_ms": round(elapsed, 2), "status": r.status_code})
        except Exception:
            performance_results.append({"endpoint": endpoint, "message": "-", "time_ms": -1, "status": "ERROR"})
    
    if response_times:
        metrics["performance"] = {
            "avg_response_time_ms": round(np.mean(response_times), 2),
            "min_response_time_ms": round(min(response_times), 2),
            "max_response_time_ms": round(max(response_times), 2),
            "median_response_time_ms": round(np.median(response_times), 2),
            "p95_response_time_ms": round(np.percentile(response_times, 95), 2),
            "successful_requests": successful,
            "failed_requests": failed,
            "success_rate": round(successful / (successful + failed) * 100, 2) if (successful + failed) > 0 else 0,
        }
        
        # --- GRAFIK 8: Response Time Distribution ---
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
        # Histogram
        ax1.hist(response_times, bins=10, color=COLORS["primary"], edgecolor="white", linewidth=1.5)
        ax1.axvline(np.mean(response_times), color=COLORS["danger"], linestyle="--", linewidth=2, label=f"Ortalama: {np.mean(response_times):.0f}ms")
        ax1.axvline(np.median(response_times), color=COLORS["success"], linestyle="--", linewidth=2, label=f"Median: {np.median(response_times):.0f}ms")
        ax1.set_xlabel("Yanit Suresi (ms)")
        ax1.set_ylabel("Frekans")
        ax1.set_title("Sekil 8a: /api/chat Yanit Sure Dagilimi", fontweight="bold")
        ax1.legend()
        # Bar per request
        ax2.bar(range(len(response_times)), response_times, color=COLORS["secondary"], edgecolor="white", linewidth=1.5)
        ax2.set_xlabel("Istek No")
        ax2.set_ylabel("Yanit Suresi (ms)")
        ax2.set_title("Sekil 8b: Sirali API Yanit Sureleri", fontweight="bold")
        plt.tight_layout()
        plt.savefig(os.path.join(FIG_DIR, "fig8_response_times.png"))
        plt.close()
        
        print(f"  OK: Ortalama {np.mean(response_times):.0f}ms, basari %{successful/(successful+failed)*100:.1f}")
    else:
        metrics["performance"] = {"error": "No successful API calls"}
        print("  UYARI: API testleri basarisiz")

except Exception as e:
    metrics["performance"] = {"error": str(e), "note": "Backend sunucusunun calistigindan emin olun"}
    print(f"  UYARI: Backend test edilemedi: {e}")

df_perf = pd.DataFrame(performance_results)
df_perf.to_csv(os.path.join(TAB_DIR, "table5_performance.csv"), index=False, encoding="utf-8-sig")


# =====================================================================
# 6. SPOTIFY INTEGRATION METRICS
# =====================================================================
print("[6/6] Spotify entegrasyon metrikleri...")

music_client = MusicClient()
spotify_status = music_client.get_status()

# Sarkilarin Spotify URL'si var mi?
songs_with_spotify_url = sum(1 for s in DEMO_SONGS if s.get("spotify_url") and s["spotify_url"] != "" and s["spotify_url"] != "#none")
songs_without_spotify = len(DEMO_SONGS) - songs_with_spotify_url

metrics["spotify_integration"] = {
    "spotify_api_available": spotify_status.get("spotify", {}).get("available", False),
    "demo_mode": spotify_status.get("demo_mode", True),
    "songs_with_spotify_url": songs_with_spotify_url,
    "songs_without_spotify_url": songs_without_spotify,
    "spotify_url_coverage_pct": round(songs_with_spotify_url / len(DEMO_SONGS) * 100, 2),
}

# --- GRAFIK 9: Spotify Coverage ---
fig, ax = plt.subplots(figsize=(7, 7))
sizes = [songs_with_spotify_url, songs_without_spotify]
labels = [f"Spotify URL Var\n({songs_with_spotify_url} sarki)", f"Spotify URL Yok\n({songs_without_spotify} sarki)"]
colors = [COLORS["spotify"], "#cccccc"]
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90, textprops={"fontsize": 11})
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontweight("bold")
    autotext.set_fontsize(14)
ax.set_title("Sekil 9: Veri Setinde Spotify URL Kapsamasi", fontsize=13, fontweight="bold", pad=15)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig9_spotify_coverage.png"))
plt.close()

print(f"  OK: Spotify URL kapsamasi %{metrics['spotify_integration']['spotify_url_coverage_pct']:.1f}")


# =====================================================================
# METRICS JSON & MARKDOWN REPORT
# =====================================================================
print()
print("Metrikler kaydediliyor...")

metrics["generated_at"] = datetime.now().isoformat()
metrics["report_version"] = "1.0"

with open(os.path.join(REPORT_DIR, "metrics.json"), "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2, ensure_ascii=False)

# Markdown rapor
md_lines = []
md_lines.append("# DJ AI - Proje Sonuc Raporu")
md_lines.append("")
md_lines.append(f"**Olusturma Tarihi:** {datetime.now().strftime('%d %B %Y, %H:%M')}")
md_lines.append("")
md_lines.append("---")
md_lines.append("")

md_lines.append("## 1. Ozet")
md_lines.append("")
md_lines.append("| Metrik | Deger |")
md_lines.append("|--------|-------|")
md_lines.append(f"| Toplam Sarki | {metrics['dataset']['total_songs']} |")
md_lines.append(f"| Unique Sanatci | {metrics['dataset']['unique_artists']} |")
md_lines.append(f"| Mevcut Tur | {metrics['dataset']['total_genres']} |")
md_lines.append(f"| Intent Classification Dogrulugu | %{metrics['intent_classification']['overall_accuracy']} |")
md_lines.append(f"| Turkce Ek Isleme Dogrulugu | %{metrics['turkish_suffix']['accuracy']} |")
md_lines.append(f"| Sarki Onerisi Alaka Duzeyi (Ort.) | %{metrics['song_relevance']['average_relevance']} |")
if "avg_response_time_ms" in metrics.get("performance", {}):
    md_lines.append(f"| Ortalama API Yanit Suresi | {metrics['performance']['avg_response_time_ms']:.0f} ms |")
    md_lines.append(f"| API Basari Orani | %{metrics['performance']['success_rate']} |")
md_lines.append(f"| Spotify URL Kapsamasi | %{metrics['spotify_integration']['spotify_url_coverage_pct']} |")
md_lines.append("")

md_lines.append("## 2. Veri Seti Istatistikleri")
md_lines.append("")
md_lines.append("![Tur Dagilimi](figures/fig1_genre_distribution.png)")
md_lines.append("")
md_lines.append("![Dil Dagilimi](figures/fig2_language_pie.png)")
md_lines.append("")
md_lines.append("![Donem Dagilimi](figures/fig3_decade_distribution.png)")
md_lines.append("")
md_lines.append("![Mood ve Activity](figures/fig4_mood_activity.png)")
md_lines.append("")

md_lines.append("## 3. Intent Classification Sonuclari")
md_lines.append("")
md_lines.append(f"Toplam **{metrics['intent_classification']['total_pass'] + metrics['intent_classification']['total_fail']} test** ile sistemin niyet tespit dogrulugu olculmustur. ")
md_lines.append(f"Genel dogruluk: **%{metrics['intent_classification']['overall_accuracy']}**")
md_lines.append("")
md_lines.append("![Intent Accuracy](figures/fig5_intent_accuracy.png)")
md_lines.append("")
md_lines.append("![Confusion Matrix](figures/fig6_confusion_matrix.png)")
md_lines.append("")
md_lines.append("### Kategori Bazli Dogruluk")
md_lines.append("")
md_lines.append("| Kategori | Basarili | Basarisiz | Dogruluk |")
md_lines.append("|----------|----------|-----------|----------|")
for cat, info in metrics["intent_classification"]["by_category"].items():
    cat_name = {"genre": "Tur", "mood": "Ruh Hali", "activity": "Aktivite", "artist": "Sanatci", "greeting": "Selamlama", "playlist": "Playlist"}.get(cat, cat)
    md_lines.append(f"| {cat_name} | {info['pass']} | {info['fail']} | %{info['accuracy']} |")
md_lines.append("")

md_lines.append("## 4. Turkce Ek Isleme Testleri")
md_lines.append("")
md_lines.append(f"Turkce dilbilgisi eklerinin (-de, -da, -e, -a, -i, -u, vb.) dogru islenmesi test edilmistir.")
md_lines.append(f"Toplam {metrics['turkish_suffix']['total_tests']} testten **{metrics['turkish_suffix']['pass']} basarili** (%{metrics['turkish_suffix']['accuracy']})")
md_lines.append("")

md_lines.append("## 5. Sarki Onerisi Alaka Duzeyi")
md_lines.append("")
md_lines.append(f"Her tur icin oneri sisteminin **alakali sarki onerme orani** olculmustur. Ortalama: **%{metrics['song_relevance']['average_relevance']}**")
md_lines.append("")
md_lines.append("![Song Relevance](figures/fig7_genre_relevance.png)")
md_lines.append("")

md_lines.append("## 6. Performans Olcumleri")
md_lines.append("")
if "avg_response_time_ms" in metrics.get("performance", {}):
    perf = metrics["performance"]
    md_lines.append("| Metrik | Deger |")
    md_lines.append("|--------|-------|")
    md_lines.append(f"| Ortalama Yanit Suresi | {perf['avg_response_time_ms']:.0f} ms |")
    md_lines.append(f"| Median Yanit Suresi | {perf['median_response_time_ms']:.0f} ms |")
    md_lines.append(f"| Min Yanit Suresi | {perf['min_response_time_ms']:.0f} ms |")
    md_lines.append(f"| Max Yanit Suresi | {perf['max_response_time_ms']:.0f} ms |")
    md_lines.append(f"| P95 Yanit Suresi | {perf['p95_response_time_ms']:.0f} ms |")
    md_lines.append(f"| Basarili Istek | {perf['successful_requests']} |")
    md_lines.append(f"| Basarisiz Istek | {perf['failed_requests']} |")
    md_lines.append(f"| Basari Orani | %{perf['success_rate']} |")
    md_lines.append("")
    md_lines.append("![Response Times](figures/fig8_response_times.png)")
else:
    md_lines.append("Performans testleri yapilamadi. Backend sunucusunun calistigindan emin olun.")
md_lines.append("")

md_lines.append("## 7. Spotify Entegrasyonu")
md_lines.append("")
si = metrics["spotify_integration"]
md_lines.append(f"- **Spotify API durumu:** {'Aktif' if si['spotify_api_available'] else 'Demo modu (API anahtari yok)'}")
md_lines.append(f"- **Spotify URL'li sarki:** {si['songs_with_spotify_url']}")
md_lines.append(f"- **Toplam kapsama:** %{si['spotify_url_coverage_pct']}")
md_lines.append("")
md_lines.append("![Spotify Coverage](figures/fig9_spotify_coverage.png)")
md_lines.append("")

md_lines.append("## 8. Sonuc")
md_lines.append("")
md_lines.append("Bu rapor, DJ AI muzik oneri sisteminin temel metriklerini icermektedir:")
md_lines.append("")
md_lines.append(f"- Sistem **{metrics['dataset']['total_songs']} sarki**, **{metrics['dataset']['unique_artists']} sanatci** ve **{metrics['dataset']['total_genres']} tur** uzerinde calismaktadir.")
md_lines.append(f"- Niyet tespit dogrulugu **%{metrics['intent_classification']['overall_accuracy']}** olarak olculmustur.")
md_lines.append(f"- Turkce ek isleme **%{metrics['turkish_suffix']['accuracy']}** basari ile gerceklestirilmistir.")
md_lines.append(f"- Sarki onerisi alaka duzeyi ortalama **%{metrics['song_relevance']['average_relevance']}**'tir.")
if "avg_response_time_ms" in metrics.get("performance", {}):
    md_lines.append(f"- API ortalama yanit suresi **{metrics['performance']['avg_response_time_ms']:.0f} ms** olup, basari orani **%{metrics['performance']['success_rate']}**'dir.")
md_lines.append("")
md_lines.append("---")
md_lines.append(f"*Rapor otomatik olusturuldu: {datetime.now().strftime('%d.%m.%Y %H:%M')}*")

with open(os.path.join(REPORT_DIR, "REPORT.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print()
print("=" * 70)
print("RAPOR BASARIYLA OLUSTURULDU")
print("=" * 70)
print(f"Konum: {os.path.abspath(REPORT_DIR)}")
print()
print("Olusturulan dosyalar:")
print(f"  - REPORT.md           (Markdown rapor)")
print(f"  - metrics.json        (Tum metrikler JSON)")
print(f"  - figures/*.png       (9 grafik)")
print(f"  - tables/*.csv        (5 tablo)")
print()
print("OZET METRIKLER:")
print(f"  Toplam Sarki:                  {metrics['dataset']['total_songs']}")
print(f"  Intent Classification:         %{metrics['intent_classification']['overall_accuracy']}")
print(f"  Turkce Ek Isleme:              %{metrics['turkish_suffix']['accuracy']}")
print(f"  Sarki Onerisi Alaka Duzeyi:    %{metrics['song_relevance']['average_relevance']}")
if "avg_response_time_ms" in metrics.get("performance", {}):
    print(f"  Ortalama API Yanit Suresi:     {metrics['performance']['avg_response_time_ms']:.0f} ms")
    print(f"  API Basari Orani:              %{metrics['performance']['success_rate']}")
print(f"  Spotify URL Kapsamasi:         %{metrics['spotify_integration']['spotify_url_coverage_pct']}")
