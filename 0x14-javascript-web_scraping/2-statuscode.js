#!/usr/bin/node
// solve task
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    console.log('code:', response.statusCode);
  }
});
