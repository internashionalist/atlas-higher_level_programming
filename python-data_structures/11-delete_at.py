#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):  # if index out of range
        return my_list  # return list as is
    del my_list[idx]  # delete element at index
    return my_list  # return modified list
