#!/usr/bin/node

const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let row = '';
  for (let n = 0; n < num; n++) {
    row += 'X';
  }
  console.log(row);
}
