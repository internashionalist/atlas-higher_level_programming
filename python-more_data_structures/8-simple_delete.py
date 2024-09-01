#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  # if key exists in dictionary
        del a_dictionary[key]  # delete key-value pair
    return a_dictionary  # return updated dictionary
