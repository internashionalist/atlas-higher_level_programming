#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):  # print matrix of integers
    for row in matrix:  # iterate through matrix
        for i in range(len(row)):  # iterate through row
            print("{:d}".format(row[i]), end="")  # print element
            if i < len(row) - 1:  # print space if not last element
                print(" ", end="")
        print()  # print newline
