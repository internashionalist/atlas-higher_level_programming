#!/usr/bin/node

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const movie of data.results) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  }
});
