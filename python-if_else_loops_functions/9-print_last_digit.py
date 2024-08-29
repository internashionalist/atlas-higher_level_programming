#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # get last digit using modulo
    print(last_digit, end='')  # print last digit
    return last_digit # return it
