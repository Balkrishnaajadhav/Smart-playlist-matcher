import os
from pathlib import Path

root = Path(__file__).parent

required_files = [
    'app.py',
    'build_catalog.py',
    'feature_extraction.py',
    'matcher.py',
    'database.py',
    'train_mood_model.py',
    'requirements.txt',
    'README.md',
]

required_dirs = [
    'catalog',
    os.path.join('catalog','audio'),
    'model',
    'logs'
]

placeholders = {
    'app.py': """# Placeholder app.py
print('app.py placeholder - create your Gradio app here or restore original file')
""",
    'build_catalog.py': """# Placeholder build_catalog.py
print('build_catalog.py placeholder')
""",
    'train_mood_model.py': """# Placeholder train_mood_model.py
print('train_mood_model.py placeholder')
""",
    'database.py': """# Placeholder database.py
print('database.py placeholder')
""",
}

print('Verifying project structure...')

for d in required_dirs:
    p = root / d
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
        print(f'Created directory: {p.relative_to(root)}')
    else:
        print(f'Exists: {p.relative_to(root)}')

for f in required_files:
    p = root / f
    if not p.exists():
        content = placeholders.get(f, '')
        p.write_text(content)
        print(f'Created placeholder file: {p.relative_to(root)}')
    else:
        print(f'Exists: {p.relative_to(root)}')

# Ensure catalog mapping and CSV exist
mapping = root / 'catalog' / 'track_mood_mapping.csv'
catalog_csv = root / 'catalog' / 'catalog_features.csv'
if not mapping.exists():
    mapping.write_text('track_id,mood\n')
    print('Created placeholder: catalog/track_mood_mapping.csv')
else:
    print('Exists: catalog/track_mood_mapping.csv')

if not catalog_csv.exists():
    catalog_csv.write_text('')
    print('Created placeholder: catalog/catalog_features.csv')
else:
    print('Exists: catalog/catalog_features.csv')

# Ensure model pickles exist as placeholders (do not create binary pickles). Create small marker files.
model_marker = root / 'model' / 'README_MODEL_PLACEHOLDER.txt'
if not model_marker.exists():
    model_marker.write_text('Model files should be stored here: mood_model.pkl and label_encoder.pkl')
    print('Created model placeholder marker')
else:
    print('Exists: model/README_MODEL_PLACEHOLDER.txt')

print('\nVerification complete. Review created placeholders and replace with real implementations/models as needed.')
