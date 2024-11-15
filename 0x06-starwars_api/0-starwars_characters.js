#!/usr/bin/node

const request = require('request');

// Convert request to promise-based function
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      resolve(JSON.parse(body));
    });
  });
}

// Main function to get and display characters
async function getMovieCharacters(movieId) {
  try {
    // Get movie data
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    const movieData = await makeRequest(movieUrl);

    // Get all characters data (maintaining order)
    const characterPromises = movieData.characters.map(url => makeRequest(url));
    const characters = await Promise.all(characterPromises);

    // Print character names in order
    characters.forEach(character => console.log(character.name));
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Get movie ID from command line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

getMovieCharacters(movieId);
