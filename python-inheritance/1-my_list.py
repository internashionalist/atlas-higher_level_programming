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
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
        return list_copy
