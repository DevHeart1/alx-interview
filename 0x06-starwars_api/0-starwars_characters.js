#!/usr/bin/node

/**
 * Enhanced Star Wars API client with parallel requests and better error handling
 */

const request = require('request');

/**
 * Wrapper function for request object that allows it
 * to work with async and await
 * @param   {String} url - site url
 * @returns {Promise}    - promise object that resolves with parsed JSON response
 */
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(new Error(`Request failed: ${error.message}`));
        return;
      }
      
      if (response.statusCode !== 200) {
        reject(new Error(`Invalid response status: ${response.statusCode}`));
        return;
      }

      try {
        const data = JSON.parse(body);
        resolve(data);
      } catch (e) {
        reject(new Error(`Failed to parse response: ${e.message}`));
      }
    });
  });
}

/**
 * Fetches all character data for a movie in parallel
 * @param {Array} characterUrls - Array of character API URLs
 * @returns {Promise} - Resolves with array of character data
 */
async function fetchCharacters(characterUrls) {
  try {
    const characterPromises = characterUrls.map(url => makeRequest(url));
    const characters = await Promise.all(characterPromises);
    return characters;
  } catch (error) {
    throw new Error(`Failed to fetch characters: ${error.message}`);
  }
}

/**
 * Entry point - makes requests to Star Wars API
 * for movie info based on movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 * in order of appearance in the initial response.
 */
async function main() {
  try {
    const args = process.argv;

    if (args.length < 3) {
      console.error('Please provide a movie ID as a parameter');
      console.error('Usage: node script.js <movie_id>');
      process.exit(1);
    }

    const movieId = args[2];
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    
    console.log(`Fetching data for Star Wars Episode ${movieId}...`);
    
    const movie = await makeRequest(movieUrl);
    
    if (!movie.characters || !Array.isArray(movie.characters)) {
      throw new Error('Invalid movie data: No character information found');
    }

    console.log(`Movie: ${movie.title}`);
    console.log(`Episode: ${movie.episode_id}`);
    console.log(`Director: ${movie.director}`);
    console.log('\nCharacters:');

    const characters = await fetchCharacters(movie.characters);
    
    // Print characters in order of appearance
    characters.forEach((character, index) => {
      console.log(`${index + 1}. ${character.name}`);
    });

  } catch (error) {
    console.error('\nError:', error.message);
    if (error.message.includes('Invalid response status')) {
      console.error('Tip: Make sure you provided a valid movie ID');
    }
    process.exit(1);
  }
}

// Add error handler for uncaught promises
process.on('unhandledRejection', (error) => {
  console.error('Unhandled promise rejection:', error);
  process.exit(1);
});

main();