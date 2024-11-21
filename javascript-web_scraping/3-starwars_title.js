#!/usr/bin/node

const request = require('request');
const movID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + movID, (error, response, body) => {
  if (error) {
    console.error('code: ' + error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
