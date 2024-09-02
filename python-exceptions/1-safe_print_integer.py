#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # print integer
        return True  # return True if successful
    except (ValueError, TypeError):
        return False  # otherwise, return False
