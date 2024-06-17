// MovieDetails.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const MovieDetails = () => {
  const { title } = useParams(); // Capture title from URL
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMovieDetails = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/movie/${encodeURIComponent(title)}`);
        setMovie(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching movie details:', error);
        setError('Error fetching movie details. Please try again later.');
        setLoading(false);
      }
    };

    fetchMovieDetails();
  }, [title]);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div className="container mt-5">
      <div className="card">
        <img src={movie.image} className="card-img-top" alt={movie.title} />
        <div className="card-body">
          <h5 className="card-title">{movie.title}</h5>
          <p className="card-text">Year: {movie.year}</p>
          <p className="card-text">Genre: {movie.genre}</p>
          <p className="card-text">{movie.description}</p>
        </div>
      </div>
    </div>
  );
};

export default MovieDetails;
