#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (n !== 0 && !isNaN(n)) {
    return n * factorial(n - 1);
  } else {
    return 1;
  }
}

console.log(factorial(n));
