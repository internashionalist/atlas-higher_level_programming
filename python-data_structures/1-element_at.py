#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):  # check if idx is out of range
        return None  # if True, return None
    return my_list[idx]  # return element at idx
