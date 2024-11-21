#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const tasks = {};
  data.forEach(task => {
    if (task.completed === true) {
      if (tasks[task.userID] === undefined) {
        tasks[task.userID] = 1;
      } else {
        tasks[task.userID]++;
      }
    }
  });
  console.log(tasks);
});
