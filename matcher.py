import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recommend_tracks(input_features, input_bpm, input_mood, weight=0.5):
    catalog = pd.read_csv("catalog/catalog_features.csv")

    # Ensure BPM is numeric
    catalog["bpm"] = pd.to_numeric(catalog["bpm"], errors="coerce")
    catalog = catalog.dropna(subset=["bpm"])

    # Select ONLY feature columns (f0, f1, f2, ...)
    feature_columns = [col for col in catalog.columns if col.startswith("f")]

    # 🔒 Ensure consistent feature length
    catalog_features = catalog[feature_columns].values
    input_features = np.array(input_features).reshape(1, -1)

    # If feature length mismatch → hard stop
    if catalog_features.shape[1] != input_features.shape[1]:
        raise ValueError(
            f"Feature mismatch: input={input_features.shape[1]}, catalog={catalog_features.shape[1]}"
        )

    # Mood filtering
    candidates = catalog[catalog["mood"] == input_mood]
    if candidates.empty:
        candidates = catalog.copy()

    # BPM filtering (±8%)
    bpm_low = input_bpm * 0.92
    bpm_high = input_bpm * 1.08

    candidates = candidates[
        (candidates["bpm"] >= bpm_low) &
        (candidates["bpm"] <= bpm_high)
    ]

    if candidates.empty:
        candidates = catalog.copy()

    candidate_features = candidates[feature_columns].values

    similarities = cosine_similarity(
        input_features,
        candidate_features
    )[0]

    candidates = candidates.copy()
    candidates["score"] = similarities

    return candidates.sort_values("score", ascending=False).head(5)[
        ["track_id", "score"]
    ]
