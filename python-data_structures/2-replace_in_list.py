#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # check if idx is out of range
        return my_list  # if out of range, return list unchanged
    my_list[idx] = element  # replace element at idx
    return my_list  # return modified list
