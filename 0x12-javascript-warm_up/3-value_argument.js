#!/usr/bin/node
const myArguments = process.argv.length;
const argsToPrint = process.argv[2];
if (myArguments === 2) {
  console.log('No argument');
} else {
  console.log(argsToPrint);
}
