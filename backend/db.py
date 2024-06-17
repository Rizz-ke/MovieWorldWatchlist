import sqlite3

def create_connection():
    conn = sqlite3.connect("movies.db")
    return conn, conn.cursor()

def initialize_database():
    conn, cursor = create_connection()
    create_genres_table(cursor)
    create_movies_table(cursor)
    create_upcoming_movies_table(cursor)
    conn.commit()
    conn.close()

def create_genres_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)

def create_movies_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        year INTEGER NOT NULL,
        genre TEXT NOT NULL,
        image TEXT
    )
    """)

def create_upcoming_movies_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS upcomingmovies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        year INTEGER NOT NULL,
        genre TEXT NOT NULL,
        image TEXT
    )
    """)

def insert_genre(name):
    conn, cursor = create_connection()
    cursor.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def fetch_all_genres():
    conn, cursor = create_connection()
    cursor.execute("SELECT * FROM genres")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_genre_by_id(genre_id):
    conn, cursor = create_connection()
    cursor.execute("SELECT * FROM genres WHERE id = ?", (genre_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def delete_genre_by_id(genre_id):
    conn, cursor = create_connection()
    cursor.execute("DELETE FROM genres WHERE id = ?", (genre_id,))
    conn.commit()
    conn.close()

def close_connection():
    conn, cursor = create_connection()
    conn.close()