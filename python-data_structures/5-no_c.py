#!/usr/bin/python3

def no_c(my_string):  # concat string, remove cC
    new_string = "".join([char for char in my_string if char not in "cC"])
    return new_string  # return new string
