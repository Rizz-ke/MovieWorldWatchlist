import sqlite3

class Genre:
    TABLE_NAME = 'genres'

    def __init__(self, name):
        self.id = None
        self.name = name

    def save(self):
        conn, cursor = create_connection()
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (name)
        VALUES (?)
        """
        try:
            cursor.execute(sql, (self.name,))
            conn.commit()
            self.id = cursor.lastrowid
            print(f"Inserted genre with ID: {self.id}")
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @classmethod
    def get_all(cls):
        conn, cursor = create_connection()
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()
        return [cls.row_to_instance(row) for row in rows]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        genre = cls(name=row[1])
        genre.id = row[0]
        return genre

    @classmethod
    def create_table(cls):
        conn, cursor = create_connection()
        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """
        try:
            cursor.execute(sql_create)
            conn.commit()
            print(f"Table '{cls.TABLE_NAME}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

    @classmethod
    def get_by_id(cls, genre_id):
        conn, cursor = create_connection()
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE id = ?"
        cursor.execute(sql, (genre_id,))
        row = cursor.fetchone()
        conn.close()
        return cls.row_to_instance(row)

    @classmethod
    def get_by_name(cls, name):
        conn, cursor = create_connection()
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE name = ?"
        cursor.execute(sql, (name,))
        row = cursor.fetchone()
        conn.close()
        return cls.row_to_instance(row) if row else None

    @classmethod
    def delete_by_id(cls, genre_id):
        conn, cursor = create_connection()
        sql = f"DELETE FROM {cls.TABLE_NAME} WHERE id = ?"
        cursor.execute(sql, (genre_id,))
        conn.commit()
        conn.close()

def create_connection():
    conn = sqlite3.connect("movies.db")
    return conn, conn.cursor()

def initialize_database():
    Genre.create_table()
    insert_initial_genres()

def insert_initial_genres():
    initial_genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Sci-Fi", "Thriller"]
    for genre in initial_genres:
        existing_genre = Genre.get_by_name(genre)
        if not existing_genre:
            genre_instance = Genre(name=genre)
            genre_instance.save()
        else:
            print(f"Genre '{genre}' already exists.")

# Initialize the database and insert initial genres
if __name__ == "__main__":
    initialize_database()