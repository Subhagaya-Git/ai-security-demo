import sqlite3

def get_user(username):
    # Insecure SQL query (SQL Injection risk)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Accidentally left a secret
API_KEY = "sk-1234567890abcdef"
