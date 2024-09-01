#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()  # copy dictionary
    for key in new_dict:  # iterate over keys in dictionary
        new_dict[key] *= 2  # multiply value by 2
    return new_dict  # return updated dictionary
