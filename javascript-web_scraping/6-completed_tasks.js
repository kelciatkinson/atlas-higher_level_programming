#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });
    console.log(completedTasks);
  } else {
    process.exit(1);
  }
});
