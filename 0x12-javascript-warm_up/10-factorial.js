#!/usr/bin/node
const firstInt = parseInt(process.argv[2]);
function getFactorial (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    return (a * getFactorial(a - 1));
  }
}
console.log(getFactorial(firstInt));
