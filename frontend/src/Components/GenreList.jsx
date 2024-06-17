// GenreList.jsx
import React from 'react';

const GenreList = ({ genres }) => {
  return (
    <>
      {genres.map((genre, index) => (
        <li key={index}>
          <a className="dropdown-item" href="#">{genre}</a>
        </li>
      ))}
    </>
  );
};

export default GenreList;
