#!/usr/bin/node

const num = process.argv[2];

for (let i = 0; i < num; i++) {
  let row = '';
  for (let n = 0; n < num; n++) {
    row += 'X';
  }
  console.log(row);
}
