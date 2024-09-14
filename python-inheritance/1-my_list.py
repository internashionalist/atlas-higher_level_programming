#!/usr/bin/python3

"""
Module adds print_sorted method to MyList class
"""


class MyList(list):
    """
    inherits from list

    Attributes:
        list (list): list to inherit from

    Methods:
        print_sorted: prints the list sorted

    Returns:
        sorted list
    """

    def print_sorted(self):
        """
        Prints list in ascending order using sorted()
        """
        sorted_list = sorted(self)  # sorted() returns a new list
        print(sorted(self))  # print the new list
        return sorted_list  # return the new list
