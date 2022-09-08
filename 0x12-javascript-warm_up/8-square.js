#!/usr/bin/node
const sqSize = process.argv[2];
let i;
if (isNaN(sqSize)) {
  console.log('Missing size');
} else {
  for (i = 0; i < sqSize; i++) {
    console.log('X'.repeat(sqSize));
  }
}
