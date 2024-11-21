#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) throw error;
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
