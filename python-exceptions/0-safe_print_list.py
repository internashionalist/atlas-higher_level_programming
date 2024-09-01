#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements = 0  # initialize count
    for i in range(x):  # iterate through x
        try:
            print(my_list[i], end="")  # print element
            elements += 1  # increment count
        except IndexError:  # if index error
            pass  # pass, stop iteration
    print()  # print newline
    return elements  # return count
