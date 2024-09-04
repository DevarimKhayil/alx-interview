#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API for the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);
  const characters = data.characters;

  // Iterate over the characters and make a request for each
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

