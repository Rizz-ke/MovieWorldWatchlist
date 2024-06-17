// server.js

const express = require('express');
const app = express();
const PORT = 8000;

// Example movies data (in-memory for demonstration purposes)
const movies = [
  { id: 1, title: 'The Fall Guy', year: 2023, genre: 'Action' },
  { id: 2, title: 'Furiosa', year: 2024, genre: 'Action' },
  // Add more movies as needed
];

// Middleware to parse JSON request bodies
app.use(express.json());

// Endpoint to fetch movie details by title
app.get('/movies/:title', (req, res) => {
  const title = req.params.title;
  const movie = movies.find(movie => movie.title.toLowerCase() === title.toLowerCase());
  if (!movie) {
    return res.status(404).json({ error: 'Movie not found' });
  }
  res.json(movie);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
