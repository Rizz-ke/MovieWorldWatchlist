// MovieCard.js
import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import './MovieCard.css';

const MovieCard = ({ movie, addToWatchlist }) => {
  const defaultImageUrl = 'https://i.pinimg.com/736x/67/24/6c/67246c540cef5ddc27ff4c11b6223e84.jpg';

  // Destructure movie object for cleaner code
  const { title, image, year, genre } = movie;

  return (
    <div className="card">
      <img
        src={image || defaultImageUrl}
        alt={title}
        className="card-image"
      />
      <div className="card-body">
        <h5 className="card-title">Title: {title}</h5>
        <p className="card-info">Year: {year}</p>
        <p className="card-info">Genre: {genre}</p>
        <Link to={`/movie/${encodeURIComponent(title)}`} className="btn btn-primary">
          View Details
        </Link>
        <button
          type="button"
          className="btn btn-secondary mt-2"
          onClick={() => addToWatchlist(movie)}
        >
          Add to Watchlist
        </button>
      </div>
    </div>
  );
};

// PropTypes for type checking
MovieCard.propTypes = {
  movie: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string,
    year: PropTypes.number.isRequired,
    genre: PropTypes.string.isRequired,
  }).isRequired,
  addToWatchlist: PropTypes.func.isRequired,
};

export default MovieCard;
