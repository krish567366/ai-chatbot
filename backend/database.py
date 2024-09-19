# backend/database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY,
            text TEXT,
            feedback TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_feedback(text, feedback):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO feedback (text, feedback) VALUES (?, ?)', (text, feedback))
    conn.commit()
    conn.close()

init_db()
