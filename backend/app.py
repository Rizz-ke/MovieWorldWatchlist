from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import movies  # Import the movies model
from db import initialize_database, close_connection, fetch_all_movies, fetch_movie_by_id

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes

@app.on_event("startup")
async def startup_event():
    initialize_database()

@app.on_event("shutdown")
async def shutdown_event():
    close_connection()

# Create a movie
@app.post("/movies/", response_model=movies)
def create_movie(movie: movies):
    movies = fetch_all_movies()
    movies.append(movie)
    return movie

# Retrieve all movies
@app.get("/movies/", response_model=list[movies])  # Corrected here
def read_movies():
    return fetch_all_movies()

# Retrieve a movie by index
@app.get("/movies/{movie_id}", response_model=movies)
def read_movie(movie_id: int):
    movie = fetch_movie_by_id(movie_id)
    if movie:
        return movie
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

# Update a movie
@app.put("/movies/{movie_id}", response_model=movies)
def update_movie(movie_id: int, movie: movies):
    movies = fetch_all_movies()
    if 0 <= movie_id < len(movies):
        movies[movie_id] = movie
        return movie
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

# Delete a movie
@app.delete("/movies/{movie_id}", response_model=movies)
def delete_movie(movie_id: int):
    movies = fetch_all_movies()
    if 0 <= movie_id < len(movies):
        deleted_movie = movies.pop(movie_id)
        return deleted_movie
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)