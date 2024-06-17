// src/Components/Home.jsx
import React, { useEffect, useState } from 'react';
import MovieCard from './MovieCard';
import './Home.css'; // Import CSS file for Home component
import { Container, Col, Carousel } from 'react-bootstrap';
import { useParams } from 'react-router-dom';

const Home = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedGenre, setSelectedGenre] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const { genre } = useParams(); // Get genre parameter from URL

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        console.log("Fetching movies...");
        const response = await fetch('http://localhost:8000/movies', {
          method: 'GET',
          headers: {
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Expires': '0'
          }
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log("Fetched movies:", data);
        // Ensure image URLs are correct
        const updatedMovies = data.map(movie => ({
          ...movie,
          imageUrl: `http://localhost:8000${movie.imageUrl}`
        }));
        setMovies(updatedMovies);
        setLoading(false);
      } catch (error) {
        setError('Error fetching movies');
        console.error('Error fetching movies:', error);
        setLoading(false);
      }
    };

    fetchMovies();
  }, []);

  const addToWatchlist = (movie) => {
    const watchlist = JSON.parse(localStorage.getItem('watchlist')) || [];
    if (!watchlist.some(watchedMovie => watchedMovie.title === movie.title)) {
      watchlist.push(movie);
      localStorage.setItem('watchlist', JSON.stringify(watchlist));
    }
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleGenreChange = (e) => {
    setSelectedGenre(e.target.value);
  };

  // Filter movies based on title, genre, and selectedGenre state
  const filteredMovies = movies.filter((movie) => {
    return (
      movie.title.toLowerCase().includes(searchTerm.toLowerCase()) &&
      (selectedGenre ? movie.genre.includes(selectedGenre) : true) &&
      (genre ? movie.genre.toLowerCase() === genre.toLowerCase() : true) // Filter by URL genre parameter
    );
  });

  // Custom image URLs for carousel
  const customImageUrls = [
    'https://mecinemas.com/assets/img/posters/TheFallGuyDub_banner.jpg',
    'https://www.tribe.games/wp-content/uploads/2024/03/ATLAS-poster-CUT1.webp',
    'https://i.pinimg.com/564x/50/cd/9b/50cd9b1615015d1cdc044f76b4b7f47b.jpg',
    'https://i.pinimg.com/564x/b1/69/40/b16940d4ab22628fdc178d14df78b547.jpg',
    'https://i.pinimg.com/564x/bd/ac/60/bdac60edd7d4268a54511d58aa0c7ce4.jpg',
  ];

  return (
    <div className="home-background">
      {/* Carousel */}
      <div className="carousel-container mb-4">
        <Carousel className="full-width-carousel">
          {customImageUrls.map((url, index) => (
            <Carousel.Item key={index}>
              <img
                className="d-block w-100"
                src={url}
                alt={`Slide ${index}`}
              />
              <Carousel.Caption>
                <h3>{filteredMovies[index]?.title}</h3>
              </Carousel.Caption>
            </Carousel.Item>
          ))}
        </Carousel>
      </div>

      {/* Search Input */}
      <div className="row mb-3">
        <div className="col-md-12">
          <input
            type="text"
            className="form-control"
            placeholder="Search for movies..."
            value={searchTerm}
            onChange={handleSearchChange}
          />
        </div>
      </div>

      {/* Filter by Genre */}
      <div className="row mb-3">
        <div className="col-md-12">
          <select
            className="form-control"
            value={selectedGenre}
            onChange={handleGenreChange}
          >
            <option value="">All Genres</option>
            {[...new Set(movies.map((movie) => movie.genre))].map((genre, index) => (
              <option key={index} value={genre}>
                {genre}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Movie Cards */}
      <div className="row">
        {loading ? (
          <p>Loading...</p>
        ) : error ? (
          <p>{error}</p>
        ) : (
          filteredMovies.map((movie, index) => (
            <Col key={index} xs={12} sm={6} md={4} lg={3}>
              <MovieCard movie={movie} addToWatchlist={addToWatchlist} />
            </Col>
          ))
        )}
      </div>

      {/* Footer */}
      <footer className="footer mt-5">
        <div className="container">
          <div className="row">
            <div className="col-md-12">
              <p>&copy; 2024 MovieWorld. All rights reserved.</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Home;