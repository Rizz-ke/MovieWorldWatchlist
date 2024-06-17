import sqlite3

class UpcomingMovies:
    TABLE_NAME = "upcomingmovies"
    
    def __init__(self, title, year, genre, image=None):
        self.id = None
        self.title = title
        self.year = year
        self.genre = genre
        self.image = image
        
    def save(self):
        conn, cursor = create_connection()
        cursor.execute(f"SELECT id FROM {self.TABLE_NAME} WHERE title = ?", (self.title,))
        result = cursor.fetchone()
        if result:
            print(f"Movie '{self.title}' already exists.")
        else:
            sql = f"""
            INSERT INTO {self.TABLE_NAME} (title, year, genre, image)
            VALUES (?, ?, ?, ?)
            """    
            try:
                cursor.execute(sql, (self.title, self.year, self.genre, self.image))
                conn.commit()
                self.id = cursor.lastrowid
                print(f"Upcoming movie '{self.title}' saved.")
            except sqlite3.IntegrityError as e:
                print(f"Error saving movie: {e}")
            finally:
                conn.close()
            
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "image": self.image
        }
        
    @classmethod
    def get_all(cls):
        conn, cursor = create_connection()
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        rows = cursor.fetchall()
        conn.close()
        return [cls.row_to_instance(row) for row in rows]
            
    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        
        movie = cls(
            title=row[1],
            year=row[2],
            genre=row[3],
            image=row[4]
        )        
        movie.id = row[0]
        return movie
        
    @classmethod
    def create_table(cls):
        conn, cursor = create_connection()
        sql = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            image TEXT
        )
        """
        try:
            cursor.execute(sql)
            conn.commit()
            print("Upcoming movies table created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

    @classmethod
    def get_by_title(cls, title):
        conn, cursor = create_connection()
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE title = ?"
        cursor.execute(sql, (title,))
        row = cursor.fetchone()
        conn.close()
        return cls.row_to_instance(row) if row else None

def create_connection():
    conn = sqlite3.connect("movies.db")
    return conn, conn.cursor()

def initialize_database():
    UpcomingMovies.create_table()
    insert_initial_movies()

def insert_initial_movies():
    # Example of inserting initial movies
    movies = [
        {"title": "Damsel", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/35/db/fc/35dbfc08a385fff295e29de0564c85ba.jpg"},
        {"title": "Imaginary", "year": "2024", "genre": "Action", "image": "https://xl.movieposterdb.com/24_03/2024/26658104/xl_imaginary-movie-poster_da8e0ffb.jpg"},
        {"title": "Kung Fu Panda 4", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/45/a8/11/45a8116b603df5fea328e8c4279eb431.jpg"},
        {"title": "Road House", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/31/64/98/316498d4792d4fb515906f7a4b7d8f66.jpg"},
        {"title": "Arthur the King", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/a8/3f/05/a83f05599fa2b43d92fe2dc7f728848f.jpg"},
        {"title": "Ghostbusters: Frozen Empire", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/ae/06/d1/ae06d169199e9635a338f48218cdd4e1.jpg"},
        {"title": "Immaculate", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/cc/b9/8f/ccb98f1647a2bdf401e017bbd0f8bb33.jpg"},
        {"title": "Godzilla x Kong: The New Empire", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/11/70/51/1170510d3027fca35c93275ca8ef8c35.jpg"},
        {"title": "Monkey Man", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/87/f4/71/87f471704d8ec9d8c031d8b8477e310c.jpg"},
        {"title": "The First Omen", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/56/ec/74/56ec74a71381dfd13c985adf62452660.jpg"},
        {"title": "Civil War", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/10/3f/e9/103fe93ccaba46975b8f6ab9fad2cbd5.jpg"},
        {"title": "Rebel Moon: Part II", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/27/df/93/27df93dbdb5de393ae6eb80422527f5e.jpg"},
        {"title": "The Ministry of Ungentlemanly Warfare", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/ad/18/65/ad1865075a5697ebeffcdea449af322b.jpg"},
        {"title": "Boy Kills World", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/a4/c4/ef/a4c4effcada700465af624321b2c9072.jpg"},
        {"title": "Challengers", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/ee/29/ee/ee29ee3e7ec50f0e89da6222590e3c65.jpg"},
        {"title": "Back to Black", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/08/95/6d/08956d7f5556c7d8cc24d0809a683f09.jpg"},
        {"title": "Horrorscope", "year": "2024", "genre": "Action", "image": "https://i.goojara.to/mb_229_229579.jpg"},
        {"title": "Kingdom of the Planet of the Apes", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/9e/51/3b/9e513bf1a63ab463d26aeced44c36640.jpg"},
        {"title": "My Ex-Friend's Wedding", "year": "2024", "genre": "Action", "image": "https://images.squarespace-cdn.com/content/v1/63bb3e8a824d7e2f7eedf0d3/e69a990a-891f-4371-af70-a39943409dfc/My+Ex+Friend%27s+Wedding+2.jpeg?format=500w"},
        {"title": "IF", "year": "2024", "genre": "Action", "image": "https://i.goojara.to/mb_229_229571.jpg"},
        {"title": "Garfield", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/e4/e3/53/e4e353929a70115b32bb7ef90ebc0f88.jpg"},
        {"title": "Bad Boys 4", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/0c/4d/6f/0c4d6f52590d28126d9009f4174b759b.jpg"},
        {"title": "Hit Man", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/7b/c1/b5/7bc1b5120902446fe80e4e95a6d0c3b9.jpg"},
        {"title": "The Watchers", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/e7/b7/46/e7b746ad9df1dad00fa06546bf251bdf.jpg"},
        {"title": "Inside Out 2", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/7d/9d/d5/7d9dd59eb9abb04c8e43494f150af4b7.jpg"},
        {"title": "A Quiet Place: Day One", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/df/83/3f/df833f11811a479a243048b3344c71f0.jpg"},
        {"title": "Mufasa: The Lion King", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/03/28/87/0328873a64e006b58c59bfc6f8f3b427.jpg"},
        {"title": "Unsung Hero", "year": "2024", "genre": "Action", "image": "https://i.goojara.to/mb_229_229592.jpg"}
    ]
    for movie in movies:
        existing_movie = UpcomingMovies.get_by_title(movie["title"])
        if not existing_movie:
            movie_instance = UpcomingMovies(**movie)
            movie_instance.save()

# Initialize the database and insert initial movies
if __name__ == "__main__":
    initialize_database()