#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    integers = 0  # initialize count
    for i in range(x):  # iterate through x
        try:
            print("{:d}".format(my_list[i]), end="")  # print integer
            integers += 1  # increment count
        except (ValueError, TypeError):  # if error
            continue  # skip that element
        except IndexError:  # if index is out of range
            break  # stop
    print()  # print newline
    return integers  # return count
