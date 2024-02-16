#!/usr/bin/node
let max = parseInt(process.argv[2]);
let secondMax = 0;
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 3; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      secondMax = max;
      max = process.argv[i];
    } else if (parseInt(process.argv[i]) > secondMax) {
      secondMax = parseInt(process.argv[i]);
    }
  }
  console.log(secondMax);
}
