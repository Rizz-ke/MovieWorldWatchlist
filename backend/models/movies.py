import sqlite3

class Movie:
    TABLE_NAME = 'movies'

    def __init__(self, title, year, genre, image=None):
        self.id = None
        self.title = title
        self.year = year
        self.genre = genre
        self.image = image

    def save(self):
        conn, cursor = create_connection()
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (title, year, genre, image)
        VALUES (?,?,?,?)
        """
        try:
            cursor.execute(sql, (self.title, self.year, self.genre, self.image))
            conn.commit()
            self.id = cursor.lastrowid
            print(f"Inserted movie '{self.title}' with ID: {self.id}")
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'genre': self.genre,
            'image': self.image
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
        movie = cls(title=row[1], year=row[2], genre=row[3], image=row[4])
        movie.id = row[0]
        return movie

    @classmethod
    def create_table(cls):
        conn, cursor = create_connection()
        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            image TEXT
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
    def get_by_id(cls, movie_id):
        conn, cursor = create_connection()
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE id =?"
        cursor.execute(sql, (movie_id,))
        row = cursor.fetchone()
        conn.close()
        return cls.row_to_instance(row)

    @classmethod
    def get_by_title(cls, title):
        conn, cursor = create_connection()
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE title =?"
        cursor.execute(sql, (title,))
        row = cursor.fetchone()
        conn.close()
        return cls.row_to_instance(row) if row else None

    @classmethod
    def delete_by_id(cls, movie_id):
        conn, cursor = create_connection()
        sql = f"DELETE FROM {cls.TABLE_NAME} WHERE id =?"
        cursor.execute(sql, (movie_id,))
        conn.commit()
        conn.close()

def create_connection():
    conn = sqlite3.connect("movies.db")
    return conn, conn.cursor()

def initialize_database():
    Movie.create_table()
    insert_initial_movies()

def insert_initial_movies():
    movies_data = [
           {
        
        "title": "The Fall Guy",
        "year": 2024,
        "genre": "Action, Comedy, Drama",
        "image": "https://i.pinimg.com/736x/c2/93/8e/c2938eea3c9b81a0feddd24d82edf161.jpg"
    },
    {
        
        "title": "Atlas",
        "year": 2024,
        "genre": "Action, Adventure, Drama",
        "image": "https://i.goojara.to/mb_229_229575.jpg"
    },
    {
        
        "title": "Furiosa",
        "year": 2024,
        "genre": "Action",
        "image": "https://i.goojara.to/mb_229_229581.jpg"
    },
    {
        
        "title": "Dune: Part Two",
        "year": 2023,
        "genre": "Sci-Fi",
        "image": "https://cdn.moviestillsdb.com/storage/posters/e8/15239678_150.jpg"
    },
    {
        
        "title": "Mission: Impossible – Dead Reckoning Part One",
        "year": 2023,
        "genre": "Action, Adventure, Thriller",
        "image": "https://i.pinimg.com/564x/a9/8c/b6/a98cb6d14371d1978ccefb838c505798.jpg"
    },
    {
       
        "title": "The Marvels",
        "year": 2023,
        "genre": "Action, Adventure, Fantasy",
        "image": "https://i.pinimg.com/564x/96/42/33/9642338bc05e332a644973975cb2b714.jpg"
    },
    {
       
        "title": "Guardians of the Galaxy Vol. 3",
        "year": 2023,
        "genre": "Action, Adventure, Comedy",
        "image": "https://i.pinimg.com/564x/69/32/1a/69321a161eb9383ec02a7b1dca141a28.jpg"
    },
    {
        
        "title": "John Wick: Chapter 4",
        "year": 2023,
        "genre": "Action, Crime, Thriller",
        "image": "https://i.pinimg.com/564x/5b/c6/2a/5bc62a7bcd1ca0e3b755ad8756857802.jpg"
    },
    {
        
        "title": "The Flash",
        "year": 2023,
        "genre": "Action, Adventure, Fantasy",
        "image": "https://i.pinimg.com/564x/70/dd/60/70dd60deb53fb34cc7ef2c28ffb14005.jpg"
    },
    {
        
        "title": "Indiana Jones and the Dial of Destiny",
        "year": 2023,
        "genre": "Action, Adventure",
        "image": "https://i.pinimg.com/564x/c9/43/9e/c9439ee778dfe060aca0bd04bf7f0865.jpg"
    },
    {
       
        "title": "Aquaman and the Lost Kingdom",
        "year": 2023,
        "genre": "Action, Adventure, Fantasy",
        "image": "https://i.pinimg.com/564x/3d/57/f4/3d57f4099776444ab365fc82e55386cb.jpg"
    },
    {
        
        "title": "Spider-Man: Across the Spider-Verse",
        "year": 2023,
        "genre": "Animation, Action, Adventure",
        "image": "https://i.pinimg.com/736x/f3/1e/12/f31e1230a68817d9b8baf4297b7ad5ec.jpg"
    },
    {
        
        "title": "Transformers: Rise of the Beasts",
        "year": 2023,
        "genre": "Action, Adventure, Sci-Fi",
        "image": "https://i.pinimg.com/564x/fe/a5/a9/fea5a9d2d259a2d4fe39aef2a1e57be5.jpg"
    },
    {
        
        "title": "Wonka",
        "year": 2023,
        "genre": "Adventure, Comedy, Family",
        "image": "https://i.pinimg.com/564x/72/c5/dd/72c5dd66d01f56712d5b5b303c26ebac.jpg"
    },
    {
        
        "title": "Oppenheimer",
        "year": 2023,
        "genre": "Biography, Drama, History",
        "image": "https://i.pinimg.com/564x/16/3a/f3/163af33dafe4fb877483ab1ddd8a0d2e.jpg"
    },
    {
        
        "title": "The Hunger Games: The Ballad of Songbirds & Snakes",
        "year": 2023,
        "genre": "Action, Adventure, Drama",
        "image": "https://i.pinimg.com/564x/6f/f4/34/6ff434b2ec6a46a82e38a0e74c4d87b5.jpg"
    },
    {
       
        "title": "Barbie",
        "year": 2023,
        "genre": "Adventure, Comedy, Fantasy",
        "image": "https://i.pinimg.com/564x/60/76/6d/60766d2782ae8cea2756ea2a6ad542fd.jpg"
    },
    {
        
        "title": "The Little Mermaid",
        "year": 2023,
        "genre": "Adventure, Family, Fantasy",
        "image": "https://i.pinimg.com/564x/8e/fa/8a/8efa8a7ed972b926eb9ce7e5e1b1d6b0.jpg"
    },
    {
        
        "title": "Fast X",
        "year": 2023,
        "genre": "Action, Adventure, Crime",
        "image": "https://i.pinimg.com/564x/9c/59/20/9c5920d5720d7ba34ebf02096d6cc94e.jpg"
    },
    {
        
        "title": "Elemental",
        "year": 2023,
        "genre": "Animation, Adventure, Comedy",
        "image": "https://i.pinimg.com/564x/43/81/29/438129a06f5c67c900a607b54e3dafeb.jpg"
    },
    {
        
        "title": "The Exorcist: Believer",
        "year": 2023,
        "genre": "Horror, Mystery, Thriller",
        "image": "https://i.goojara.to/mb_229_229099.jpg"
    },
    {
        
        "title": "Shazam! Fury of the Gods",
        "year": 2023,
        "genre": "Action, Adventure, Comedy",
        "image": "https://i.pinimg.com/564x/ae/91/1b/ae911b0a601e99b1482a01ffaab20da2.jpg"
    },
    {
        
        "title": "Scream VI",
        "year": 2023,
        "genre": "Horror, Mystery, Thriller",
        "image": "https://i.pinimg.com/564x/2d/b8/40/2db840114ea6e2aa85f3235afc69536e.jpg"
    },
    {
        
        "title": "Evil Dead Rise",
        "year": 2023,
        "genre": "Horror, Thriller",
        "image": "https://i.pinimg.com/564x/b5/96/9f/b5969f831d59dfff730c57dbaf83dbc2.jpg"
    },
    {
        
        "title": "Blue Beetle",
        "year": 2023,
        "genre": "Action, Adventure, Sci-Fi",
        "image": "https://i.pinimg.com/564x/52/b4/63/52b463a7135e06f0d55d0d81bd56d0dc.jpg"
    },
    {
        
        "title": "The Shift",
        "year": 2023,
        "genre": "Sci-Fi",
        "image": "https://i.goojara.to/mb_229_229437.jpg"
    },
    {
        
        "title": "Haunted Mansion",
        "year": 2023,
        "genre": "Comedy, Drama, Family",
        "image": "https://i.pinimg.com/564x/91/09/4b/91094b24696bfdc14fd40f3c322ca94a.jpg"
    },
    {
        
        "title": "Insidious: The Red Door",
        "year": 2023,
        "genre": "Horror, Mystery, Thriller",
        "image": "https://i.pinimg.com/564x/8d/1b/75/8d1b7570d37ace4090d6f232fd9c9246.jpg"
    },
    {
        
        "title": "The Nun II",
        "year": 2023,
        "genre": "Horror, Mystery, Thriller",
        "image": "https://i.pinimg.com/564x/b6/7c/a5/b67ca574aaaab20328f10a25e8dcbb2f.jpg"
    },
    {
        
        "title": "The Equalizer 3",
        "year": 2023,
        "genre": "Action, Crime, Thriller",
        "image": "https://i.pinimg.com/564x/79/5e/99/795e99cbd5181fdf2ed80bb3f13bd6c2.jpg"
    },
    {
        
        "title": "Last Shift",
        "year": 2014,
        "genre": "Horror",
        "image": "https://i.goojara.to/mb_225_225959.jpg"
    },
    {
        
        "title": "Migration",
        "year": 2023,
        "genre": "Animation",
        "image": "https://i.pinimg.com/564x/b9/78/52/b978529695d2fa5de1fdb5bc92b2dbd1.jpg"
    },
    {
        
        "title": "Dune: Part Two",
        "year": 2023,
        "genre": "Sci-Fi",
        "image": "https://i.pinimg.com/564x/7a/76/05/7a7605972d2e5209e200e689400e953a.jpg"
    },
    {
        
        "title": "Malang",
        "year": 2023,
        "genre": "Action",
        "image": "https://i.pinimg.com/564x/2f/a2/67/2fa267077fbac52b51ad75d0a1e2d15b.jpg"
    },
    {
        
        "title": "Mooned",
        "year": 2023,
        "genre": "Animation",
        "image": "https://i.goojara.to/mb_229_229427.jpg"
    },
    {
        
        "title": "Ferrari",
        "year": 2023,
        "genre": "Drama",
        "image": "https://i.goojara.to/mb_229_229384.jpg"
    },
    {
       
        "title": "The Re-Education of Molly Singer",
        "year": 2023,
        "genre": "Comedy",
        "image": "https://i.goojara.to/mb_229_229516.jpg"
    },
    {
        
        "title": "Godzilla minus one",
        "year": 2023,
        "genre": "Adventure",
        "image": "https://i.goojara.to/mb_229_229539.jpg"
    },
    {
        
        "title": "Greed",
        "year": 2022,
        "genre": "Drama",
        "image": "https://i.goojara.to/mb_229_229341.jpg"
    },
    {
        
        "title": "8: A South African Horror Story",
        "year": 2022,
        "genre": "Horror",
        "image": "https://i.goojara.to/mb_225_225005.jpg"
    }
    ]

    for movie_data in movies_data:
        movie = Movie(
            title=movie_data["title"],
            year=movie_data["year"],
            genre=movie_data["genre"],
            image=movie_data["image"]
        )
        if not Movie.get_by_title(movie.title):
            movie.save()
        else:
            print(f"Movie '{movie.title}' already exists.")

if __name__ == "__main__":
    initialize_database()