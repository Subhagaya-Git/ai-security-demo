import sqlite3

def get_user(username):
    # Secure: Use parameterized query to prevent SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?" 
    cursor.execute(query, (username,))
    return cursor.fetchall()

# Removed the hardcoded API_KEY