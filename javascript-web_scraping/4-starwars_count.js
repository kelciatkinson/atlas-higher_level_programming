#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterID = '18';

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body);
    let count = 0;
    for (const film of films.results) {
      for (const char of film.characters) {
        if (char.endsWith(`/${characterID}/`)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
