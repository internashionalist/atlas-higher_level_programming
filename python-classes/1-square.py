#!/usr/bin/python3

"""
this module defines geometric class Square.
"""


class Square:
    """
    class represents a square.

    attributes:
        size (int): length of the sides of a square.
    """

    def __init__(self, size):
        """
        initialize new Square instance.
        """
        self.__size = size  # size is private
