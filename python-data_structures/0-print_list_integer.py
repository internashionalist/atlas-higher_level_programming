#!/usr/bin/python3

def print_list_integer(my_list=[]):  # use my_list as default argument
    for number in my_list:  # iterate through my_list
        print("{:d}".format(number))  # print number
