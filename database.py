import sqlite3
from datetime import datetime

# Create database connection
connection = sqlite3.connect("automation_logs.db", check_same_thread=False)
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    time TEXT,
    status TEXT,
    error TEXT,
    analysis TEXT
)
""")
connection.commit()

def save_log(status, error, analysis):
    """
    Saves automation result to database
    """
    cursor.execute(
        "INSERT INTO logs VALUES (?, ?, ?, ?)",
        (str(datetime.now()), status, error, analysis)
    )
    connection.commit()
