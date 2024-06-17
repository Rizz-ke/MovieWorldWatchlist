import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './UpcomingMovies.css'; // Import CSS file for styling

function UpcomingMovies() {
    const [movies, setMovies] = useState([]); // Initialize movies state as an empty array
    const [loading, setLoading] = useState(true); // Loading state for fetching data
    const [error, setError] = useState(null); // Error state for fetching data

    useEffect(() => {
        fetchMovies();
    }, []);

    const fetchMovies = async () => {
        try {
            const response = await axios.get('http://localhost:8000/upcoming-movies');
            setMovies(response.data); // Assuming response.data is an array of movies
            setLoading(false); // Set loading to false after fetching data
        } catch (error) {
            console.error('Error fetching upcoming movies:', error);
            setError('Error fetching data. Please try again later.'); // Set error message
            setLoading(false); // Set loading to false on error
        }
    };

    if (loading) {
        return <p>Loading...</p>; // Display loading message while fetching data
    }

    if (error) {
        return <p>{error}</p>; // Display error message if fetching data fails
    }

    if (!Array.isArray(movies) || movies.length === 0) {
        return <p>No movies found.</p>; // Display a message if no movies are found
    }

    return (
        <div className="movies-container">
            <h2>Upcoming Movies</h2>
            <div className="card-container">
                {movies.map(movie => (
                    <div key={movie.title} className="card">
                        <img src={movie.image} alt={movie.title} className="card-image" />
                        <div className="card-content">
                            <h3 className="card-title">{movie.title}</h3>
                            <p className="card-year">Year: {movie.year}</p>
                            <p className="card-genre">Genre: {movie.genre}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default UpcomingMovies;
