import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "travelsathi.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # TRIPS TABLE (IMPORTANT)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS trips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    destination TEXT NOT NULL,
    start_date TEXT,
    days INTEGER,
    people INTEGER,
    hotel_type TEXT,
    travel_mode TEXT,
    travel_class TEXT,
    total_budget REAL,
    created_at TEXT
)
""")


    conn.commit()
    conn.close()
