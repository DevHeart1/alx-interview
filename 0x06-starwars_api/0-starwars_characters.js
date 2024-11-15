#!/usr/bin/node
const request = require('request');

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function getMovieCharacters (movieId) {
  try {
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    const movieData = await makeRequest(movieUrl);

    const characterPromises = movieData.characters.map(url => makeRequest(url));
    const characters = await Promise.all(characterPromises);

    characters.forEach(character => console.log(character.name));
  } catch (error) {
    console.error(error);
  }
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
