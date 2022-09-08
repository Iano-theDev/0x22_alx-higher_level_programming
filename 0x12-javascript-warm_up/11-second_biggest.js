#!/usr/bin/node
const myInts = process.argv.slice(2);
let secondBiggest = 0;
if (myInts.length > 1) {
  myInts.sort(function (a, b) {
    return a - b;
  });
  secondBiggest = myInts.slice(-2, -1);
}
console.log(parseInt(secondBiggest));
