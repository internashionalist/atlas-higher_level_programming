#!/usr/bin/python3

def common_elements(set_1, set_2):
    commons = set()  # set to store common elements
    for i in set_1:  # iterate through set_1
        if i in set_2:  # check if element is in set_2
            commons.add(i)  # add to the set if it is
    return commons  # return set
