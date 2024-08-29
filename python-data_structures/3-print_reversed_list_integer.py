#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for number in reversed(my_list):  # iterate through reversed list
        print("{:d}".format(number))  # print number
