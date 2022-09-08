#!/usr/bin/node
const firstInt = process.argv[2];
const secondInt = process.argv[3];
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    return (parseInt(a) + parseInt(b));
  }
}
console.log(add(firstInt, secondInt));
