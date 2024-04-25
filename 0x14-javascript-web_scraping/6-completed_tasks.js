#!/usr/bin/node
// solve task
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const tasks = {};
    for (const task of todos) {
      if (task.completed) {
        if (tasks[task.userId]) {
          tasks[task.userId]++;
        } else {
          tasks[task.userId] = 1;
        }
      }
    }
    console.log(tasks);
  }
});
