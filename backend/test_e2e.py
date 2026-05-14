import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from analyzer import MessageAnalyzer, ResponseGenerator
from demo_data import DEMO_SONGS

analyzer = MessageAnalyzer()
generator = ResponseGenerator(songs_db=DEMO_SONGS)

test_cases = [
    ("Rock muzik oner", {"genre": "rock", "type": "genre"}),
    ("Turkce rap dinlemek istiyorum", {"genre": "turkce_rap", "type": "genre"}),
    ("Uzgunum", {"mood": "uzgun", "type": "mood"}),
    ("Derse calisirken muzik oner", {"activity": "ders", "type": "activity"}),
    ("Spor yaparken dinleyecegim", {"activity": "spor", "type": "activity"}),
    ("Gece yolculugu icin", {"activity": "gece", "type": "activity"}),
    ("Lo-fi muzik oner", {"genre": "lofi", "type": "genre"}),
    ("Arabesk sarkilar oner", {"genre": "arabesk", "type": "genre"}),
    ("Mutlu edici sarkilar", {"mood": "mutlu", "type": "mood"}),
    ("Enerjik hissediyorum", {"mood": "enerjik", "type": "mood"}),
    ("Merhaba", {"type": "greeting"}),
    ("Selam", {"type": "greeting"}),
    ("Tarkan dinlemek istiyorum", {"artist": "Tarkan", "type": "artist"}),
    ("Baris Manco oner", {"artist": "Baris Manco", "type": "artist"}),
    ("Kislik muzik oner", {"activity": "kislik", "type": "activity"}),
    ("Yagmurlu havada ne dinleyeyim", {"activity": "yagmur", "type": "activity"}),
    ("10 sarkilik karisik playlist yap", {"type": "playlist_count"}),
    ("Pop ve rock karisik oner", {"type": "multi_genre"}),
    ("Sakinlesmek istiyorum", {"mood": "sakin", "type": "mood"}),
    ("Derse calismaya yardimci muzik", {"activity": "ders", "type": "activity"}),
]

print("=" * 70)
print("MUZIKBOT ANALYSIS & PLAYLIST TEST")
print("=" * 70)

failures = []

for msg, expected in test_cases:
    result = analyzer.analyze(msg)
    response = generator.generate_response(msg, result)
    
    status = "PASS"
    exp_type = expected["type"]
    
    if exp_type == "genre" and result.get("genre") != expected["genre"]:
        status = f"FAIL (expected genre={expected['genre']}, got {result.get('genre')})"
        failures.append((msg, expected, result))
    elif exp_type == "mood" and result.get("mood") != expected["mood"]:
        status = f"FAIL (expected mood={expected['mood']}, got {result.get('mood')})"
        failures.append((msg, expected, result))
    elif exp_type == "activity" and result.get("activity") != expected["activity"]:
        status = f"FAIL (expected activity={expected['activity']}, got {result.get('activity')})"
        failures.append((msg, expected, result))
    elif exp_type == "artist" and result.get("artist") != expected["artist"]:
        status = f"FAIL (expected artist={expected['artist']}, got {result.get('artist')})"
        failures.append((msg, expected, result))
    elif exp_type == "greeting":
        if result.get("confidence", 0) > 0.2:
            status = f"FAIL (greeting detected as non-greeting, conf={result.get('confidence')})"
            failures.append((msg, expected, result))
        if len(response.get("songs", [])) > 0:
            status = f"FAIL (greeting returned songs: {len(response['songs'])})"
            failures.append((msg, expected, result))
    elif exp_type == "playlist_count" and result.get("is_playlist_request") != True:
        status = f"FAIL (expected playlist request, got {result.get('is_playlist_request')})"
        failures.append((msg, expected, result))
    elif exp_type == "multi_genre" and len(result.get("genres", [])) < 2:
        status = f"FAIL (expected multi-genre, got {result.get('genres')})"
        failures.append((msg, expected, result))
    
    songs_count = len(response.get("songs", []))
    print(f"  [{status.split(' ')[0]}] \"{msg}\" -> genre={result.get('genre')}, mood={result.get('mood')}, activity={result.get('activity')}, artist={result.get('artist')}, songs={songs_count}")

print()
if failures:
    print(f"FAILURES ({len(failures)}):")
    for msg, expected, result in failures:
        print(f"  '{msg}': expected {expected}, got genre={result.get('genre')} mood={result.get('mood')} activity={result.get('activity')} artist={result.get('artist')}")
else:
    print("ALL TESTS PASSED!")

print()
print("=" * 70)
print("TURKISH SUFFIX TESTS (strict=False for moods/activities)")
print("=" * 70)

suffix_tests = [
    ("Derse calisiyorum", "activity", "ders"),
    ("Spora gidecegim", "activity", "spor"),
    ("Uykum gelmiyor", "activity", "uyku"),
    ("Mutluyum bugun", "mood", "mutlu"),
    ("Uzgunum arkadasim", "mood", "uzgun"),
    ("Enerjik hissediyorum", "mood", "enerjik"),
    ("Sakinlesmek istiyorum", "mood", "sakin"),
    ("Geceye selam", "activity", "gece"),
    ("Yoldayim", "activity", "yolculuk"),
]

suffix_failures = []
for msg, check_type, expected_val in suffix_tests:
    result = analyzer.analyze(msg)
    actual = result.get(check_type)
    status = "PASS" if actual == expected_val else f"FAIL (expected {expected_val}, got {actual})"
    if actual != expected_val:
        suffix_failures.append((msg, check_type, expected_val, actual))
    print(f"  [{status.split(' ')[0]}] \"{msg}\" -> {check_type}={actual}")

print()
if suffix_failures:
    print(f"SUFFIX FAILURES ({len(suffix_failures)}):")
    for msg, ct, exp, act in suffix_failures:
        print(f"  '{msg}': {ct} expected={exp}, got={act}")
else:
    print("ALL SUFFIX TESTS PASSED!")

print()
print("=" * 70)
print("PLAYLIST SONG RELEVANCE TESTS")
print("=" * 70)

genre_playlist_tests = [
    ("rock", ["rock", "indie", "alternatif_rock", "grunge", "metal"]),
    ("pop", ["pop", "turkce_pop"]),
    ("rap", ["rap", "hiphop", "trap", "turkce_rap"]),
    ("lofi", ["lofi", "ambient", "neoklasik"]),
    ("arabesk", ["arabesk", "damar", "fantazi"]),
    ("jazz", ["jazz", "blues", "soul"]),
]

for genre, related_genres in genre_playlist_tests:
    analysis = {"genre": genre, "genres": [genre], "mood": None, "activity": None, "artist": None, "language": None, "is_playlist_request": True, "playlist_count": 10, "confidence": 0.5, "keywords": [f"tur:{genre}"]}
    response = generator.generate_response(f"{genre} muzik oner", analysis)
    songs = response.get("songs", [])
    if songs:
        relevant = 0
        for s in songs:
            song_all_genres = s.get("genres", [s.get("genre", "")])
            if not isinstance(song_all_genres, list):
                song_all_genres = [song_all_genres]
            if any(rg in sg for rg in related_genres for sg in song_all_genres):
                relevant += 1
        pct = relevant / len(songs) * 100 if songs else 0
        status = "PASS" if pct >= 50 else f"WARN ({pct:.0f}% relevant)"
        print(f"  [{status}] {genre}: {relevant}/{len(songs)} songs relevant ({pct:.0f}%)")
    else:
        print(f"  [FAIL] {genre}: No songs returned")