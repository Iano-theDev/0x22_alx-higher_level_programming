#!/usr/bin/node
const myArguments = process.argv.length;
if (myArguments === 2) {
  console.log('no argument');
} else if (myArguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
