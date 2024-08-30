#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()  # copy list
    for idx, num in enumerate(new_list):  # iterate through list
        if num == search:  # when search is found
            new_list[idx] = replace  # replace it
    return new_list  # return modified list
