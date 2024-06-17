import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Login.css'; 

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // Call API to login
    const userData = { email, name: 'John Doe' }; // Replace with actual user data
    localStorage.setItem('user', JSON.stringify(userData));
    navigate('/home'); // Redirect to home page after successful login
  };

  return (
    <div className="login-background">
      <div className="login-container">
        <h2>Sign In</h2>
        <form onSubmit={handleLogin}>
          <div className="mb-3">
            <input
              type="email"
              className="form-control"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="mb-3">
            <input
              type="password"
              className="form-control"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="btn btn-primary w-100">Sign In</button>
        </form>
        <p className="mt-3">
          New to Movie World? <Link to="/signup">Sign up now</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
