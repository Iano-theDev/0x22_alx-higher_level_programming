#!/usr/bin/node
const firstArgument = process.argv[2];
if (firstArgument === undefined || isNaN(firstArgument)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArgument; i++) {
    console.log('X'.repeat(firstArgument));
  }
}
