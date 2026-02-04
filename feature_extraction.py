import librosa
import numpy as np

def extract_features(audio_path):
    """Extract exactly 30 audio features from an audio file."""
    try:
        # Load audio
        y, sr = librosa.load(audio_path, duration=60)
        
        # MFCC features (13 mean + 13 std = 26 features)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_mean = mfcc.mean(axis=1)  # 13 features
        mfcc_std = mfcc.std(axis=1)    # 13 features
        
        # Tempo (1 feature)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        if isinstance(tempo, np.ndarray):
            tempo = float(tempo[0]) if len(tempo) > 0 else 0.0
        tempo = float(tempo)
        
        # RMS Energy (2 features: mean + std)
        rms = librosa.feature.rms(y=y)[0]
        rms_mean = float(np.mean(rms))
        rms_std = float(np.std(rms))
        
        # Zero Crossing Rate (1 feature)
        zcr = librosa.feature.zero_crossing_rate(y)[0]
        zcr_mean = float(np.mean(zcr))
        
        # Combine all features into a single vector (30 features total)
        feature_vector = np.concatenate([
            mfcc_mean,      # 13 features
            mfcc_std,       # 13 features
            [tempo],        # 1 feature
            [rms_mean],     # 1 feature
            [rms_std],      # 1 feature
            [zcr_mean]      # 1 feature
        ])
        
        return feature_vector, float(tempo)
    
    except Exception as e:
        print(f"Error extracting features: {e}")
        return None, None
