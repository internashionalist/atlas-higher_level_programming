#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # new list to store results
    for i in range(list_length):  # iterate up to list_length
        try:  # try dividing elements
            result = my_list_1[i] / my_list_2[i]
