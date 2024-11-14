#!/usr/bin/node

const myVar = ['No argument', 'Argument found', 'Arguments found'];

if (process.argv.length > 3) {
  console.log(myVar[2]);
} else {
  console.log(myVar[process.argv.length - 2]);
}
