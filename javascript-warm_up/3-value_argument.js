#!/usr/local/bin/node
// print 1st argument
if (process.argv[2] == null) {
    console.log('No argument');
  } else if (process.argv[3] == null) {
    console.log(process.argv[2]);
  } else { console.log(process.argv[2]); }
  