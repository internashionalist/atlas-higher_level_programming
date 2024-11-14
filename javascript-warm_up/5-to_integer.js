#!/usr/bin/node

const int = parseInt(process.argv[2]);

if (isNaN(int)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${int}`);
}
