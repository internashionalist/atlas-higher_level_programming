#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # check if idx out of range
        return my_list.copy()  # if out of range, return list unchanged
    new_list = my_list.copy()  # copy list
    new_list[idx] = element  # replace element at idx
    return new_list  # return modified list
