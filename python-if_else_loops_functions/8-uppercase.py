#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # check if character is lowercase
            c = chr(ord(c) - 32)  # convert to uppercase
        print("{0}".format(c), end="") # print character
    print()  # print newline
