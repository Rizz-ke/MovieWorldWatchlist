import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import logo from '../assets/images/Movie logo.jpg';
import './NavBar.css';

const Navbar = () => {
  const handleLogout = () => {
    localStorage.removeItem('loggedIn');
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <div className="navbar-header">
          <Link className="navbar-brand" to="/home">
            <img src={logo} alt="Logo" className="logo-img" />
            MOVIE WORLD
          </Link>
        </div>
        <div className="welcome-text">WELCOME TO MOVIE WORLD</div>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link" to="/home" activeClassName="active" exact>
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/about" activeClassName="active">
                About
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/contact" activeClassName="active">
                Contact
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/genres" activeClassName="active">
                Genres
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/watchlist" activeClassName="active">
                Watchlist
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/upcoming-movies" activeClassName="active">
                Upcoming Movies
              </NavLink>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/login" onClick={handleLogout}>
                Logout
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
