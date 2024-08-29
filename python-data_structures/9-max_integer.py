#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:  # if list is empty
        return None  # return None
    Max = my_list[0]  # set Max to first element
    for i in my_list:  # iterate through list
        if i > Max:  # if an element is greater than Max
            Max = i  # set Max to that element
    return Max  # return Max
