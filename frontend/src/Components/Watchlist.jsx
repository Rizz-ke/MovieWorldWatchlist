// Components/Watchlist.jsx
import React, { useState, useEffect } from 'react';
import './Watchlist.css'; // Import CSS file for styling

const Watchlist = () => {
  const [watchlist, setWatchlist] = useState([]);

  useEffect(() => {
    // Retrieve watchlist from localStorage
    const storedWatchlist = JSON.parse(localStorage.getItem('watchlist')) || [];
    setWatchlist(storedWatchlist);
  }, []);

  const removeFromWatchlist = (index) => {
    const updatedWatchlist = watchlist.filter((_, i) => i !== index);
    setWatchlist(updatedWatchlist);
    localStorage.setItem('watchlist', JSON.stringify(updatedWatchlist));
  };

  return (
    <div className="container text-center mt-5 watchlist-container">
      <h1>Your Watchlist</h1>
      <div className="row">
        {watchlist.length > 0 ? (
          watchlist.map((movie, index) => (
            <div key={index} className="col-md-4 mb-4">
              <div className="card">
                <img
                  src={movie.image || 'https://i.pinimg.com/736x/67/24/6c/67246c540cef5ddc27ff4c11b6223e84.jpg'}
                  className="card-img-top"
                  alt={movie.title}
                />
                <div className="card-body">
                  <h5 className="card-title">Title: {movie.title}</h5>
                  <p className="card-text">Year: {movie.year}</p>
                  <p className="card-text">Genre: {movie.genre}</p>
                  <button
                    className="btn btn-danger"
                    onClick={() => removeFromWatchlist(index)}
                  >
                    Remove from Watchlist
                  </button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p>No movies in your watchlist.</p>
        )}
      </div>
    </div>
  );
};

export default Watchlist;
