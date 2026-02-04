import sqlite3
from datetime import datetime

def log_query(mood, bpm, tracks):
    conn = sqlite3.connect("logs/queries.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            mood TEXT,
            bpm REAL,
            tracks TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO queries (timestamp, mood, bpm, tracks) VALUES (?, ?, ?, ?)",
        (datetime.now().isoformat(), mood, bpm, ",".join(tracks))
    )

    conn.commit()
    conn.close()
