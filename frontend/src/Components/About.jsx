// About.jsx
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './About.css';

const About = () => {
  const [words, setWords] = useState([]);
  const [currentWord, setCurrentWord] = useState('');
  const [typing, setTyping] = useState(false);

  useEffect(() => {
    const wordsArray = [
      'Welcome to our Movie Watchlist App!',
      
    ];

    setWords(wordsArray.);
    setCurrentWord('');
    setTyping(true);
  }, []);

  useEffect(() => {
    if (typing) {
      const intervalId = setInterval(() => {
        if (currentWord.length < words[0].length) {
          setCurrentWord(words[0].slice(0, currentWord.length + 1));
        } else {
          setTyping(false);
        }
      }, 50);
      return () => clearInterval(intervalId);
    }
  }, [currentWord, typing, words]);

  return (
    <div className="about-container">
      <div className="about-content">
        <h1>About Us</h1>
        <p className="typing-effect">{currentWord}</p>

        {/* Features Section */}
        <div className="features-section">
          <h2>Why Choose Our App?</h2>
          <ul>
            <li>Personalized movie recommendations based on your preferences.</li>
            <li>Add movies to your watchlist and look them up later</li>
            <li>Search for movies by genre and release year</li>
            <li>Keep track of watched movies by removing them in your watchlist</li>
          </ul>
        </div>

        {/* Call to Action */}
        <div className="call-to-action">
          <h2>Get Started Today!</h2>
          <p>Join thousands of movie enthusiasts who are already enjoying our app.</p>
          <Link to="/signup" className="btn btn-primary">Sign Up Now</Link>
        </div>
      </div>
    </div>
  );
};

export default About;
