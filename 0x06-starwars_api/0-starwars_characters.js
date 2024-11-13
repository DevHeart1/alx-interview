#!/usr/bin/node
const request = require('request');

function getMovieCharacters (movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const movie = JSON.parse(body);
    const characters = movie.characters;
    let completed = 0;

    // Process characters in order
    characters.forEach((characterUrl, index) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          return;
        }

        const character = JSON.parse(charBody);
        // Store name with its index to maintain order
        characters[index] = character.name;
        completed++;

        // Print all names in order when all requests are done
        if (completed === characters.length) {
          characters.forEach(name => console.log(name));
        }
      });
    });
  });
}

// Get movie ID from command line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

getMovieCharacters(movieId);