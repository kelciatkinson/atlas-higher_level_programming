#!/usr/bin/node

const num = Number(process.argv[2]);
if (num > 0 || num <= 0) {
  console.log(`My number: ${num}`);
} else { console.log('Not a number'); }
