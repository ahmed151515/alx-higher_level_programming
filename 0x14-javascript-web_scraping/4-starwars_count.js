#!/usr/bin/node
// solve task
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (const i in results) {
      const characters = results[i].characters;
      for (const j in characters) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
