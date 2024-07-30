#!/usr/bin/node

const request = require('request');

const movie = process.argv[2];

if (!movie) {
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movie}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
