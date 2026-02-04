# 🎧 Smart Playlist Matcher

<div align="center">

![PlayMood](https://img.shields.io/badge/PlayMood-Professional%20Audio%20Analysis-6366f1?style=for-the-badge&logo=music&logoColor=white)

**AI-Powered Music Mood Detection & Recommendation System**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-UI-FF7C00?style=flat&logo=gradio&logoColor=white)](https://gradio.app)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Librosa](https://img.shields.io/badge/Librosa-Audio-green?style=flat)](https://librosa.org)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Architecture](#-system-architecture) • [Usage](#-usage)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🎯 Overview

**Smart Playlist Matcher** is an end-to-end AI-powered audio intelligence system that analyzes uploaded song clips, predicts their mood and tempo, and recommends similar tracks from a local music catalog. Built as a professional case study project, it demonstrates expertise in:

- 🎵 **Audio Signal Processing** using Librosa
- 🤖 **Machine Learning** with scikit-learn
- 🔍 **Recommendation Systems** with cosine similarity
- 🎨 **Modern UI/UX** with Gradio
- 📊 **Data Persistence** with SQLite

This system mimics core functionalities of music streaming platforms like Spotify, making it perfect for demonstrating ML engineering skills in interviews.

---

## ✨ Features

### Core Capabilities

- **🎼 Audio Feature Extraction**
  - MFCCs (Mel-Frequency Cepstral Coefficients)
  - Tempo (BPM) Detection
  - Energy & RMS Analysis
  - Zero-Crossing Rate

- **🎭 Mood Classification**
  - 4 mood categories: Happy, Calm, Energetic, Sad
  - Confidence scoring with threshold (0.55)
  - Logistic Regression model
  - Low-confidence fallback handling

- **🎯 Smart Recommendations**
  - Mood-based filtering
  - BPM similarity (±8% tolerance)
  - Cosine similarity on audio features
  - Top-5 track recommendations

- **💾 Data Persistence**
  - SQLite logging of all queries
  - Timestamp tracking
  - Query history for analysis

### UI/UX Features

- **🎨 Professional Interface**
  - Dark slate minimalist design (#0F172A)
  - Gradient accents with mood-reactive colors
  - Clean typography (Inter font)
  - Smooth button animations

- **📱 Responsive Design**
  - Mobile-friendly layout
  - Accessible controls
  - Clear visual hierarchy

- **⚡ Real-Time Processing**
  - Instant mood prediction
  - Fast feature extraction (10-60s audio)
  - Smooth transitions

---

## 🏗️ System Architecture

```
User (Gradio UI)
      ↓
Audio Upload (MP3/WAV)
      ↓
Feature Extraction (Librosa)
   ├── MFCCs (13 coefficients)
   ├── Tempo (BPM)
   ├── RMS Energy
   └── Zero-Crossing Rate
      ↓
Mood Prediction (LogisticRegression)
   ├── Confidence Score
   └── Mood Label
      ↓
Similarity Matching Engine
   ├── Mood Filter
   ├── BPM Filter (±8%)
   └── Cosine Similarity
      ↓
Top-5 Recommendations
      ↓
UI Display + SQLite Logging
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Audio Processing** | Librosa | Feature extraction, BPM detection |
| **Machine Learning** | scikit-learn | Logistic Regression for mood classification |
| **Similarity Computation** | scikit-learn | Cosine similarity for track matching |
| **Data Handling** | Pandas, NumPy | Data manipulation and numerical operations |
| **User Interface** | Gradio | Interactive web UI |
| **Database** | SQLite | Query logging and persistence |
| **Model Persistence** | joblib | Saving/loading ML models |
| **Audio File Support** | soundfile | Reading audio files |

---

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- 100MB+ free disk space

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Balkrishnaajadhav/Smart-playlist-matcher.git
   cd Smart-playlist-matcher
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Build catalog features** (first-time setup)
   ```bash
   python build_catalog.py
   ```

5. **Train the mood model**
   ```bash
   python train_mood_model.py
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:7860
   ```

---

## 📁 Project Structure

```
Smart-playlist-matcher/
│
├── app.py                      # Main Gradio application
├── build_catalog.py            # Catalog feature generator
├── feature_extraction.py       # Audio feature extraction module
├── matcher.py                  # Recommendation engine
├── database.py                 # SQLite logging module
├── train_mood_model.py         # ML model training script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
│
├── catalog/                    # Music catalog
│   ├── audio/                  # Audio files
│   │   ├── track1.mp3
│   │   ├── track2.mp3
│   │   ├── track3.mp3
│   │   └── track4.mp3
│   ├── track_mood_mapping.csv  # Manual mood labels
│   └── catalog_features.csv    # Extracted features
│
├── model/                      # Trained ML models
│   ├── mood_model.pkl          # Logistic Regression model
│   └── label_encoder.pkl       # Label encoder
│
└── logs/                       # Application logs
    └── queries.db              # SQLite database
```

---

## 🚀 Usage

### Basic Workflow

1. **Upload Audio**: Drag and drop or select an MP3/WAV file (10-60 seconds recommended)
2. **Analyze**: Click the analyze button
3. **View Results**:
   - Detected mood
   - Confidence score (%)
   - BPM (tempo)
   - Top 5 similar track recommendations

### Adding New Tracks

1. Add audio files to `catalog/audio/`
2. Update `catalog/track_mood_mapping.csv` with mood labels:
   ```csv
   File,Mood
   track5.mp3,happy
   track6.mp3,energetic
   ```
3. Rebuild catalog:
   ```bash
   python build_catalog.py
   ```
4. Retrain model:
   ```bash
   python train_mood_model.py
   ```

### Viewing Query History

Query logs are stored in `logs/queries.db`. Access via SQLite:

```bash
sqlite3 logs/queries.db
SELECT * FROM queries ORDER BY timestamp DESC LIMIT 10;
```

---

## 🔬 How It Works

### 1. Feature Extraction

The system converts audio into 30 numerical features:

**Features Extracted:**
- **13 MFCC means**: Timbre/texture characteristics
- **13 MFCC std deviations**: Variability in sound
- **1 Tempo**: Beats per minute
- **1 RMS mean**: Average loudness
- **1 RMS std**: Loudness variation
- **1 Zero-crossing rate**: Frequency content indicator

### 2. Mood Classification

Uses **Logistic Regression** trained on manually labeled data:

**Mood Categories:**
- Happy 😊
- Calm 😌
- Energetic ⚡
- Sad 😢

**Confidence Threshold**: If max probability < 0.55 → "not confident"

### 3. Recommendation Algorithm

Three-stage filtering and ranking:

1. **Mood Filter**: Prioritize tracks with same mood
2. **BPM Filter**: Accept tracks within ±8% BPM range
3. **Cosine Similarity**: Rank by feature vector similarity

### 4. Persistence Layer

All queries logged to SQLite with:
- Timestamp
- Detected mood
- BPM value
- Recommended track IDs

---

## ⚠️ Limitations

This system is designed as a **case study/demo** and has intentional limitations:

### Technical Constraints

1. **Small Dataset**: Trained on only 4 manually-labeled tracks
2. **Subjective Mood Labels**: Mood classification is inherently subjective
3. **Local Processing**: No external API integration
4. **Short Audio Clips**: Optimized for 10-60 second segments
5. **Limited Genres**: May not generalize across diverse music genres

### Known Issues

- **BPM Detection**: May be unstable for ambient or complex rhythms
- **Feature Drift**: Manual retraining required when adding new tracks
- **No Real-Time Updates**: Catalog must be rebuilt manually
- **Single-User**: No multi-user support or authentication

### Scope

- ✅ **Educational/Demo purposes**
- ✅ **Interview case study**
- ✅ **ML engineering portfolio**
- ❌ **NOT production-ready**
- ❌ **NOT suitable for large-scale deployment**

---

## 🚀 Future Enhancements

Potential improvements for production deployment:

### ML Improvements
- [ ] Expand dataset to 1000+ tracks
- [ ] Implement deep learning (CNN/RNN)
- [ ] Add more mood categories (energetic-happy, calm-sad, etc.)
- [ ] Real-time model retraining pipeline

### Features
- [ ] User authentication & profiles
- [ ] Playlist creation & management
- [ ] Spotify/Apple Music API integration
- [ ] Advanced audio visualizations
- [ ] Export results as shareable cards

### Architecture
- [ ] Microservices architecture
- [ ] Cloud deployment (AWS/GCP)
- [ ] RESTful API
- [ ] Caching layer (Redis)
- [ ] Docker containerization

### UI/UX
- [ ] Dark/light mode toggle
- [ ] Glassmorphism design system
- [ ] Animated mood-reactive backgrounds
- [ ] Progressive Web App (PWA)
- [ ] Waveform visualization

---

## 🎓 Interview Talking Points

When discussing this project in interviews:

1. **"This project demonstrates end-to-end ML engineering"**
   - Data collection & labeling
   - Feature engineering
   - Model training & evaluation
   - Production deployment (Gradio UI)
   - Monitoring (SQLite logging)

2. **"I solved a real feature mismatch bug"**
   - Debugged 29 vs 30 feature drift issue
   - Ensured feature consistency across training/inference
   - Demonstrates production ML debugging skills

3. **"The system uses interpretable ML"**
   - Logistic Regression over deep learning
   - Explainable cosine similarity
   - Human-understandable mood categories

4. **"Built with production best practices"**
   - Clean code structure
   - Modular design
   - Error handling with try-except blocks
   - Data persistence
   - Version control with Git

---

## 👤 Author

**Balkrishna Jadhav**

- 🔗 GitHub: [@Balkrishnaajadhav](https://github.com/Balkrishnaajadhav)
- 💼 LinkedIn: [Balkrishna Jadhav](https://www.linkedin.com/in/balkrishna-jadhav-2a5a58237/)
- 📧 Project Repository: [Smart-playlist-matcher](https://github.com/Balkrishnaajadhav/Smart-playlist-matcher)

---

## 🙏 Acknowledgments

- **Librosa** team for excellent audio processing library
- **scikit-learn** developers for ML tools
- **Gradio** for rapid UI development
- Open-source community for inspiration

---

## 📊 Project Stats

- **Lines of Code**: ~1,000
- **Files**: 8 Python modules
- **Dependencies**: 7 core libraries
- **Features per Track**: 30
- **Inference Time**: <3 seconds per track
- **UI Framework**: Gradio Blocks

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by Balkrishna Jadhav

[🔝 Back to Top](#-smart-playlist-matcher)

</div>
