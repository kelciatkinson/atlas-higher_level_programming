#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Error: No URL provided');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
