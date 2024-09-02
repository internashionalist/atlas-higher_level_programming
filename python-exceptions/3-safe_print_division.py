#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b  # try dividing a by b
    except ZeroDivisionError:  # if b is 0
        result = None  # set result to None
