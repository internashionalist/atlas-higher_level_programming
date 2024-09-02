#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []  # new list to store results
    for i in range(list_length):  # iterate up to list_length
        try:  # try dividing elements
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:  # if division by zero
            print("division by 0")
            result = 0
        except TypeError:  # if not int or float
            print("wrong type")
            result = 0
        except IndexError:  # if out of range
            print("out of range")
            result = 0
