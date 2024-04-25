#!/usr/bin/node
// solve task
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(filePath, body, 'utf8', function (err) {
      if (err) {
        return console.error(err);
      }
    });
  }
});
