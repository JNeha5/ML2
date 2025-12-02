import sqlite3
import pandas as pd

# Create or connect to local database file
conn = sqlite3.connect("students.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks(
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT,
    marks INTEGER
);
""")

# Insert data (only if empty)
cursor.execute("SELECT COUNT(*) FROM marks")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO marks (roll_no, name, subject, marks)
    VALUES (?, ?, ?, ?)
    """, [
        (1, "Neha", "Maths", 89),
        (2, "Amit", "Science", 76),
        (3, "Priya", "English", 92),
        (4, "Rohan", "Computers", 85)
    ])
    conn.commit()

# Fetch into pandas DataFrame
df = pd.read_sql_query("SELECT * FROM marks", conn)

print(df)
