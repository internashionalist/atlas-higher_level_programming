#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let i = 0; i < list.length; i++) {
    reversed[i] = list[list.length - i - 1];
  }
  return reversed;
};
