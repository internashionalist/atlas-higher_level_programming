#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # check if lowercase
            result += chr(ord(c) - 32)  # convert to uppercase
        else:
            result += c  # keep if already uppercase
    print("{0}".format(result))  # print result
