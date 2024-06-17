import React from 'react';
import PropTypes from 'prop-types';
import './Genre.css'; // Import your CSS file for component-specific styles

const Genre = ({ genres, movies }) => {
  // Function to group movies by genre
  const groupMoviesByGenre = () => {
    const groupedMovies = {};
    movies.forEach(movie => {
      const genre = movie.genre.toLowerCase().trim(); // Normalize genre name
      if (groupedMovies[genre]) {
        groupedMovies[genre].push(movie);
      } else {
        groupedMovies[genre] = [movie];
      }
    });
    return groupedMovies;
  };

  const groupedMovies = groupMoviesByGenre();

  // Function to render movies as cards for a specific genre
  const renderMovies = (genre) => (
    groupedMovies[genre.toLowerCase()] && groupedMovies[genre.toLowerCase()].map((movie, index) => (
      <div className="card movie-card" key={index}>
        <img src={movie.image} className="card-img-top" alt={movie.title} />
        <div className="card-body">
          <h5 className="card-title">{movie.title}</h5>
          <p className="card-text">{movie.year}</p>
        </div>
      </div>
    ))
  );

  // Function to render genres as headings, including those without movies
  const renderGenres = () => (
    <div>
      {genres.map((genre, index) => (
        <div key={index} className="genre-section">
          <h2>{genre}</h2>
          <div className="card-group">
            {renderMovies(genre)}
          </div>
          {/* Display message if no movies found in the genre */}
          {(!groupedMovies[genre.toLowerCase()] || groupedMovies[genre.toLowerCase()].length === 0) && (
            <p>No movies found in this genre</p>
          )}
        </div>
      ))}
    </div>
  );

  return (
    <div>
      <h1>Genres Page</h1>
      <div>
        <h2>All Genres</h2>
        {renderGenres()}
      </div>
    </div>
  );
};

Genre.propTypes = {
  genres: PropTypes.arrayOf(PropTypes.string).isRequired,
  movies: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      year: PropTypes.number.isRequired,
      genre: PropTypes.string.isRequired,
      image: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default Genre;
