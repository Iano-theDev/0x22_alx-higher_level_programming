#!/usr/bin/node
const argsToPrint = process.argv[2];
if (argsToPrint === undefined) {
  console.log('No argument');
} else {
  console.log(argsToPrint);
}
