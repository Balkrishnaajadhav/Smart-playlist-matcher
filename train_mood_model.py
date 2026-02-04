import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load catalog data
data = pd.read_csv("catalog/catalog_features.csv")

# Extract ONLY feature columns (f0 through f29) - exactly 30 features
feature_columns = [col for col in data.columns if col.startswith("f")]
print(f"Training with {len(feature_columns)} features")

X = data[feature_columns].values
y = data["mood"].values

# Encode mood labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

print(f"Training data shape: {X.shape}")
print(f"Classes: {encoder.classes_}")

# Train model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X, y_encoded)

# Save model and encoder
joblib.dump(model, "model/mood_model.pkl")
joblib.dump(encoder, "model/label_encoder.pkl")

print("✓ Model and encoder saved successfully!")
print(f"Model expects {model.n_features_in_} features")
