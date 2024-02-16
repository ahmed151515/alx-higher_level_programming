#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (times) {
  for (let i = 0; i < size; i++) {
    console.log('x'.repeat(size));
  }
} else {
  console.log('Missing size');
}
