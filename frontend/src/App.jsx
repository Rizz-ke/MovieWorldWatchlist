import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './Components/Navbar';
import Home from './Components/Home';
import About from './Components/About';
import Contact from './Components/Contact';
import Login from './Components/Login';
import Signup from './Components/Signup';
import Watchlist from './Components/Watchlist';
import MovieDetails from './Components/MovieDetails';
import Genre from './Components/Genre';
import UpcomingMovies from './Components/UpcomingMovies';

const App = () => {
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
    <Router>
      <Navbar genres={genres} />
      <Routes>
        <Route path="/" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/home" element={<Home movies={movies} />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/watchlist" element={<Watchlist />} />
        <Route path="/upcoming-movies" element={<UpcomingMovies />} />
        <Route path="/genres" element={<Genre genres={genres} movies={movies} />} />
        <Route path="/genres/:genreName" element={<Genre movies={movies} />} />
        <Route path="/movie/:title" element={<MovieDetails />} />
      </Routes>
    </Router>
  );
};

export default App;
