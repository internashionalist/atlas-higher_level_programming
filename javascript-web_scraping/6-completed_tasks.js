#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const tasks = {};
  data.forEach(task => {
    if (task.completed === true) {
      if (tasks[task.userId] === undefined) {
        tasks[task.userId] = 1;
      } else {
        tasks[task.userId]++;
      }
    }
  });
  console.log(tasks);
});
