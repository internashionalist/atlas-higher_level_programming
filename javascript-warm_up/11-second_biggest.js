#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(Number);

function secondBiggest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }
  numbers.sort((a, b) => a - b);
  return numbers[numbers.length - 2];
}

console.log(secondBiggest(numbers));
