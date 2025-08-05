import sqlite3

def create_database():
    conn = sqlite3.connect(database="rms.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course (CourseName TEXT, Duration TEXT, Fee TEXT, Description TEXT)")
    conn.commit()

create_database()