#!/usr/bin/node

const request = require('request');
const charID = '18';
const url = process.argv[2];

request(url + charID, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;
  films.forEach(film => {
    if (film.characters.some(char => char.includes(charID))) {
      count++;
    }
  });
  console.log(count);
});
