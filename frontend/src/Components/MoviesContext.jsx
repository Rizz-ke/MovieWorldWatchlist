// MoviesContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

const MoviesContext = createContext();

export const useMovies = () => useContext(MoviesContext);

export const MoviesProvider = ({ children }) => {
  const [movies, setMovies] = useState([]);
  const [loadingMovies, setLoadingMovies] = useState(true);
  const [errorMovies, setErrorMovies] = useState(null);
  const [genres, setGenres] = useState([]);
  const [loadingGenres, setLoadingGenres] = useState(true);
  const [errorGenres, setErrorGenres] = useState(null);

  useEffect(() => {
    fetchMovies();
    fetchGenres();
  }, []);

  const fetchMovies = async () => {
    try {
      const response = await axios.get('http://localhost:8000/movies');
      setMovies(response.data);
      setLoadingMovies(false);
    } catch (error) {
      console.error('Error fetching movies:', error);
      setErrorMovies('Error fetching movies. Please try again later.');
      setLoadingMovies(false);
    }
  };

  const fetchGenres = async () => {
    try {
      const response = await axios.get('http://localhost:8000/genres');
      setGenres(response.data);
      setLoadingGenres(false);
    } catch (error) {
      console.error('Error fetching genres:', error);
      setErrorGenres('Error fetching genres. Please try again later.');
      setLoadingGenres(false);
    }
  };

  if (loadingMovies || loadingGenres) {
    return <p>Loading...</p>;
  }

  if (errorMovies || errorGenres) {
    return (
      <p>
        {errorMovies}
        <br />
        {errorGenres}
      </p>
    );
  }

  return (
    <MoviesContext.Provider value={{ movies, genres }}>
      {children}
    </MoviesContext.Provider>
  );
};
