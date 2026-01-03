import sqlite3
from datetime import date, timedelta

DB_PATH = "database/meetings.db"

def query_meetings(question: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    if "today" in question.lower():
        d = date.today().isoformat()
        cur.execute("SELECT * FROM meetings WHERE date=?", (d,))
    elif "tomorrow" in question.lower():
        d = (date.today() + timedelta(days=1)).isoformat()
        cur.execute("SELECT * FROM meetings WHERE date=?", (d,))
    else:
        cur.execute("SELECT * FROM meetings")

    results = cur.fetchall()
    conn.close()
    return results