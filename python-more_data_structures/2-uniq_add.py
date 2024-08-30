#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniques = []  # list to store unique elements
    sum = 0  # total sum of unique elements

    for element in my_list:  # iterate through the list
        if element not in uniques:  # check if element is unique
            uniques.append(element)  # add it to the list if unique
            sum += element  # add to the total

    return sum
