import sqlite3

def create_database():
    conn = sqlite3.connect(database="rms.db")
    cur = conn.cursor()
    
    # Create course table
    cur.execute("CREATE TABLE IF NOT EXISTS course (CourseName TEXT, Duration TEXT, Fee TEXT, Description TEXT)")
    
    # Create student table with foreign key reference to course
    cur.execute("""CREATE TABLE IF NOT EXISTS student (
        roll_no TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        contact TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        admission TEXT NOT NULL,
        gender TEXT NOT NULL,
        course TEXT NOT NULL,
        address TEXT,
        FOREIGN KEY (course) REFERENCES course(CourseName)
    )""")
    
    conn.commit()
    conn.close()

create_database()