// Contact.jsx
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEnvelope, faPhone } from '@fortawesome/free-solid-svg-icons';
import { faFacebook, faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';
import './Contact.css'; // Import your custom CSS for Contact page styles

const Contact = () => {
  return (
    <div className="contact-content-container">
      <div className="container-fluid text-center mt-5 contact-container">
        <h1 className="mb-4">Contact Us</h1>
        <div className="row">
          <div className="col-md-6 mb-4">
            <div className="contact-item p-4">
              <FontAwesomeIcon icon={faEnvelope} size="3x" className="contact-icon mb-3" />
              <p className="mb-0 contact-info">contact@moviewatchlist.com</p>
            </div>
          </div>
          <div className="col-md-6 mb-4">
            <div className="contact-item p-4">
              <FontAwesomeIcon icon={faPhone} size="3x" className="contact-icon mb-3" />
              <p className="mb-0 contact-info">0712345678</p>
            </div>
          </div>
        </div>
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="feedback-form mt-5 p-4">
              <h2 className="mb-4">Send us your feedback</h2>
              <form>
                <div className="form-group">
                  <input type="text" className="form-control" placeholder="Your Name" required />
                </div>
                <div className="form-group">
                  <input type="email" className="form-control" placeholder="Your Email" required />
                </div>
                <div className="form-group">
                  <textarea className="form-control" rows="5" placeholder="Your Message" required></textarea>
                </div>
                <button type="submit" className="btn btn-primary btn-block">Submit</button>
              </form>
            </div>
          </div>
        </div>
        <div className="row justify-content-center mt-4">
          <div className="col-md-6">
            <div className="additional-info">
              <p>Connect with us on social media:</p>
              <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" className="social-link">
                <FontAwesomeIcon icon={faFacebook} size="2x" className="facebook-icon" />
              </a>
              <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="social-link">
                <FontAwesomeIcon icon={faTwitter} size="2x" className="twitter-icon" />
              </a>
              <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="social-link">
                <FontAwesomeIcon icon={faInstagram} size="2x" className="instagram-icon" />
              </a>
              <div className="mt-3">
                <p>@moviewatchlist</p>
                <p>@watchmovies</p>
                <p>@instamovies</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
