# Smart Playlist Matcher

A local prototype that analyzes audio tracks, predicts mood, and suggests matching tracks.

Repository structure (required):

Smart-playlist-matcher/
│
├── app.py
├── build_catalog.py
├── feature_extraction.py
├── matcher.py
├── database.py
├── train_mood_model.py
├── requirements.txt
│
├── catalog/
│   ├── audio/
│   │   ├── track1.mp3
│   │   ├── track2.mp3
│   │   ├── track3.mp3
│   │   └── track4.mp3
│   │
│   ├── track_mood_mapping.csv
│   └── catalog_features.csv
│
├── model/
│   ├── mood_model.pkl
│   └── label_encoder.pkl
│
├── logs/
│   └── queries.db
│
└── README.md

Quick start

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. (Optional) Rebuild catalog and train model:

```powershell
python build_catalog.py
python train_mood_model.py
```

3. Run the app:

```powershell
python app.py
```

Notes

- The repository expects the `catalog/audio/` folder to contain sample `.mp3` files.
- If any files are missing, run `ensure_structure.py` to create safe placeholders without overwriting existing files.
=======
# Smart-playlist-matcher
>>>>>>> 9123fc6536df5cd19f44ea51e172b2ec4f197c00
