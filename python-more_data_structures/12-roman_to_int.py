#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0  # if not a string or None, return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}  # dictionary of roman numerals

    numeral = 0  # initialize result
    prev = 0  # initialize previous numeral value

    for char in reversed(roman_string):  # iterate backwards
        value = roman_numerals.get(char, 0)  # get int value of current numeral
        if value < prev:
            numeral -= value  # subtract if > previous numeral
        else:
            numeral += value  # otherwise, add value
        prev = value  # update previous numeral's value

    return numeral  # return final integer value
