#!/usr/bin/node

const myVar = ["No argument", "Argument found", "Arguments found"];

if (process.argv.length > 2) {
    console.log(myVar[2]);
} 
else if (process.argv.length === 2) {
    console.log(myVar[1]);
}
else {
    console.log(myVar[0]);
}
