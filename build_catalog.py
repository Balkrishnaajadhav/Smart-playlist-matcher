import os
import pandas as pd
from feature_extraction import extract_features

AUDIO_DIR = "catalog/audio"

# Map audio files to moods
mood_map = {
    "track1.mp3": "happy",
    "track2.mp3": "calm",
    "track3.mp3": "energetic",
    "track4.mp3": "sad",
}

data = []

print("Extracting features from audio files...")

for file in os.listdir(AUDIO_DIR):
    if file.endswith((".wav", ".mp3")):
        path = os.path.join(AUDIO_DIR, file)
        print(f"  Processing {file}...", end=" ")
        
        features, bpm = extract_features(path)
        
        if features is None:
            print("FAILED")
            continue
        
        row = {
            "track_id": file,
            "mood": mood_map.get(file, "unknown"),
            "bpm": bpm
        }
        
        # Add all feature columns (f0, f1, ..., f29)
        for i, value in enumerate(features):
            row[f"f{i}"] = float(value)
        
        data.append(row)
        print(f"✓ ({len(features)} features)")

# Create DataFrame and save
df = pd.DataFrame(data)
print(f"\nCatalog summary:")
print(f"  Total tracks: {len(df)}")
print(f"  Feature columns: {len([c for c in df.columns if c.startswith('f')])}")
print(f"  Data shape: {df.shape}")

df.to_csv("catalog/catalog_features.csv", index=False)
print("✓ Catalog saved to catalog/catalog_features.csv")
