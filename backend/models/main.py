from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

initial_genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Sci-Fi", "Thriller", "Horror"]

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MOVIES = [
       {
        
        "title": "The Fall Guy",
        "year": 2024,
        "genre": "Action",
        "image": "https://i.pinimg.com/736x/c2/93/8e/c2938eea3c9b81a0feddd24d82edf161.jpg"
    },
    {
        
        "title": "Atlas",
        "year": 2024,
        "genre": "Action",
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
        "genre": "Action",
        "image": "https://i.pinimg.com/564x/a9/8c/b6/a98cb6d14371d1978ccefb838c505798.jpg"
    },
    {
       
        "title": "The Marvels",
        "year": 2023,
        "genre": " Fantasy",
        "image": "https://i.pinimg.com/564x/96/42/33/9642338bc05e332a644973975cb2b714.jpg"
    },
    {
       
        "title": "Guardians of the Galaxy Vol. 3",
        "year": 2023,
        "genre": " Comedy",
        "image": "https://i.pinimg.com/564x/69/32/1a/69321a161eb9383ec02a7b1dca141a28.jpg"
    },
    {
        
        "title": "John Wick: Chapter 4",
        "year": 2023,
        "genre": "Action",
        "image": "https://i.pinimg.com/564x/5b/c6/2a/5bc62a7bcd1ca0e3b755ad8756857802.jpg"
    },
    {
        
        "title": "The Flash",
        "year": 2023,
        "genre": " Fantasy",
        "image": "https://i.pinimg.com/564x/70/dd/60/70dd60deb53fb34cc7ef2c28ffb14005.jpg"
    },
    {
        
        "title": "Indiana Jones and the Dial of Destiny",
        "year": 2023,
        "genre": " Adventure",
        "image": "https://i.pinimg.com/564x/c9/43/9e/c9439ee778dfe060aca0bd04bf7f0865.jpg"
    },
    {
       
        "title": "Aquaman and the Lost Kingdom",
        "year": 2023,
        "genre": "Fantasy",
        "image": "https://i.pinimg.com/564x/3d/57/f4/3d57f4099776444ab365fc82e55386cb.jpg"
    },
    {
        
        "title": "Spider-Man: Across the Spider-Verse",
        "year": 2023,
        "genre": "Animation ",
        "image": "https://i.pinimg.com/736x/f3/1e/12/f31e1230a68817d9b8baf4297b7ad5ec.jpg"
    },
    {
        
        "title": "Transformers: Rise of the Beasts",
        "year": 2023,
        "genre": " Sci-Fi",
        "image": "https://i.pinimg.com/564x/fe/a5/a9/fea5a9d2d259a2d4fe39aef2a1e57be5.jpg"
    },
    {
        
        "title": "Wonka",
        "year": 2023,
        "genre": "Adventure ",
        "image": "https://i.pinimg.com/564x/72/c5/dd/72c5dd66d01f56712d5b5b303c26ebac.jpg"
    },
    {
        
        "title": "Oppenheimer",
        "year": 2023,
        "genre": " Drama",
        "image": "https://i.pinimg.com/564x/16/3a/f3/163af33dafe4fb877483ab1ddd8a0d2e.jpg"
    },
    {
        
        "title": "The Hunger Games: The Ballad of Songbirds & Snakes",
        "year": 2023,
        "genre": "Drama",
        "image": "https://i.pinimg.com/564x/6f/f4/34/6ff434b2ec6a46a82e38a0e74c4d87b5.jpg"
    },
    {
       
        "title": "Barbie",
        "year": 2023,
        "genre": "Comedy",
        "image": "https://i.pinimg.com/564x/60/76/6d/60766d2782ae8cea2756ea2a6ad542fd.jpg"
    },
    {
        
        "title": "The Little Mermaid",
        "year": 2023,
        "genre": "Adventure",
        "image": "https://i.pinimg.com/564x/8e/fa/8a/8efa8a7ed972b926eb9ce7e5e1b1d6b0.jpg"
    },
    {
        
        "title": "Fast X",
        "year": 2023,
        "genre": " Crime",
        "image": "https://i.pinimg.com/564x/9c/59/20/9c5920d5720d7ba34ebf02096d6cc94e.jpg"
    },
    {
        
        "title": "Elemental",
        "year": 2023,
        "genre": "Animation",
        "image": "https://i.pinimg.com/564x/43/81/29/438129a06f5c67c900a607b54e3dafeb.jpg"
    },
    {
        
        "title": "The Exorcist: Believer",
        "year": 2023,
        "genre": "Horror",
        "image": "https://i.goojara.to/mb_229_229099.jpg"
    },
    {
        
        "title": "Shazam! Fury of the Gods",
        "year": 2023,
        "genre": "Action",
        "image": "https://i.pinimg.com/564x/ae/91/1b/ae911b0a601e99b1482a01ffaab20da2.jpg"
    },
    {
        
        "title": "Scream VI",
        "year": 2023,
        "genre": "Horror",
        "image": "https://i.pinimg.com/564x/2d/b8/40/2db840114ea6e2aa85f3235afc69536e.jpg"
    },
    {
        
        "title": "Evil Dead Rise",
        "year": 2023,
        "genre": "Horror",
        "image": "https://i.pinimg.com/564x/b5/96/9f/b5969f831d59dfff730c57dbaf83dbc2.jpg"
    },
    {
        
        "title": "Blue Beetle",
        "year": 2023,
        "genre": "Fantasy",
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
        "genre": "Comedy",
        "image": "https://i.pinimg.com/564x/91/09/4b/91094b24696bfdc14fd40f3c322ca94a.jpg"
    },
    {
        
        "title": "Insidious: The Red Door",
        "year": 2023,
        "genre": "Thriller",
        "image": "https://i.pinimg.com/564x/8d/1b/75/8d1b7570d37ace4090d6f232fd9c9246.jpg"
    },
    {
        
        "title": "The Nun II",
        "year": 2023,
        "genre": "Thriller",
        "image": "https://i.pinimg.com/564x/b6/7c/a5/b67ca574aaaab20328f10a25e8dcbb2f.jpg"
    },
    {
        
        "title": "The Equalizer 3",
        "year": 2023,
        "genre": " Thriller",
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

UPCOMING_MOVIES = [
      {"title": "Damsel", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/35/db/fc/35dbfc08a385fff295e29de0564c85ba.jpg"},
        {"title": "Imaginary", "year": "2024", "genre": "Action", "image": "https://xl.movieposterdb.com/24_03/2024/26658104/xl_imaginary-movie-poster_da8e0ffb.jpg"},
        {"title": "Kung Fu Panda 4", "year": "2024", "genre": "Animation", "image": "https://i.pinimg.com/564x/45/a8/11/45a8116b603df5fea328e8c4279eb431.jpg"},
        {"title": "Road House", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/31/64/98/316498d4792d4fb515906f7a4b7d8f66.jpg"},
        {"title": "Arthur the King", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/a8/3f/05/a83f05599fa2b43d92fe2dc7f728848f.jpg"},
        {"title": "Ghostbusters: Frozen Empire", "year": "2024", "genre": "Thriller", "image": "https://i.pinimg.com/736x/ae/06/d1/ae06d169199e9635a338f48218cdd4e1.jpg"},
        {"title": "Immaculate", "year": "2024", "genre": "Horror", "image": "https://i.pinimg.com/736x/cc/b9/8f/ccb98f1647a2bdf401e017bbd0f8bb33.jpg"},
        {"title": "Godzilla x Kong: The New Empire", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/11/70/51/1170510d3027fca35c93275ca8ef8c35.jpg"},
        {"title": "Monkey Man", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/87/f4/71/87f471704d8ec9d8c031d8b8477e310c.jpg"},
        {"title": "The First Omen", "year": "2024", "genre": "Horror", "image": "https://i.pinimg.com/736x/56/ec/74/56ec74a71381dfd13c985adf62452660.jpg"},
        {"title": "Civil War", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/10/3f/e9/103fe93ccaba46975b8f6ab9fad2cbd5.jpg"},
        {"title": "Rebel Moon: Part II", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/27/df/93/27df93dbdb5de393ae6eb80422527f5e.jpg"},
        {"title": "The Ministry of Ungentlemanly Warfare", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/ad/18/65/ad1865075a5697ebeffcdea449af322b.jpg"},
        {"title": "Boy Kills World", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/a4/c4/ef/a4c4effcada700465af624321b2c9072.jpg"},
        {"title": "Challengers", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/ee/29/ee/ee29ee3e7ec50f0e89da6222590e3c65.jpg"},
        {"title": "Back to Black", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/08/95/6d/08956d7f5556c7d8cc24d0809a683f09.jpg"},
        {"title": "Horrorscope", "year": "2024", "genre": "Action", "image": "https://i.goojara.to/mb_229_229579.jpg"},
        {"title": "Kingdom of the Planet of the Apes", "year": "2024", "genre": "Fantasy", "image": "https://i.pinimg.com/736x/9e/51/3b/9e513bf1a63ab463d26aeced44c36640.jpg"},
        {"title": "My Ex-Friend's Wedding", "year": "2024", "genre": "Action", "image": "https://images.squarespace-cdn.com/content/v1/63bb3e8a824d7e2f7eedf0d3/e69a990a-891f-4371-af70-a39943409dfc/My+Ex+Friend%27s+Wedding+2.jpeg?format=500w"},
        {"title": "IF", "year": "2024", "genre": "Fantasy", "image": "https://i.goojara.to/mb_229_229571.jpg"},
        {"title": "Garfield", "year": "2024", "genre": "Animation", "image": "https://i.pinimg.com/736x/e4/e3/53/e4e353929a70115b32bb7ef90ebc0f88.jpg"},
        {"title": "Bad Boys 4", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/564x/0c/4d/6f/0c4d6f52590d28126d9009f4174b759b.jpg"},
        {"title": "Hit Man", "year": "2024", "genre": "Action", "image": "https://i.pinimg.com/736x/7b/c1/b5/7bc1b5120902446fe80e4e95a6d0c3b9.jpg"},
        {"title": "The Watchers", "year": "2024", "genre": "Thriller", "image": "https://i.pinimg.com/736x/e7/b7/46/e7b746ad9df1dad00fa06546bf251bdf.jpg"},
        {"title": "Inside Out 2", "year": "2024", "genre": "Animation", "image": "https://i.pinimg.com/736x/7d/9d/d5/7d9dd59eb9abb04c8e43494f150af4b7.jpg"},
        {"title": "A Quiet Place: Day One", "year": "2024", "genre": "Horror", "image": "https://i.pinimg.com/564x/df/83/3f/df833f11811a479a243048b3344c71f0.jpg"},
        {"title": "Mufasa: The Lion King", "year": "2024", "genre": "Fantasy", "image": "https://i.pinimg.com/564x/03/28/87/0328873a64e006b58c59bfc6f8f3b427.jpg"},
        {"title": "Unsung Hero", "year": "2024", "genre": "Action", "image": "https://i.goojara.to/mb_229_229592.jpg"}
    
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/movies")
def get_movies():
    return MOVIES

@app.get("/movie/{title}")
def get_movie_by_title(title: str):
    for movie in MOVIES:
        if movie["title"] == title:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/genres")
def get_genres():
    return initial_genres

@app.get("/upcoming-movies")
def get_upcoming_movies():
    return UPCOMING_MOVIES

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
