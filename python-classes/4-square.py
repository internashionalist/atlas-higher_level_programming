#!/usr/bin/python3

"""
this module defines geometric class square
"""


class Square:  # public class
    """
    class represents a square

    attributes:
        size (int): length of the sides of a square
    """

    def __init__(self, size=0):  # public instance method / constructor
        """
        initialize new instance of Square

        args: size (int): length of the sides of a square

        raises:
            TypeError: if size is not an integer
            ValueError: if size is negative
        """
        if not isinstance(size, int):  # check if size is not an integer
            raise TypeError("size must be an integer")
        elif size < 0:  # check if size is negative
            raise ValueError("size must be >= 0")
        else:  # assign size to instance
            self.__size = size  # keep size private

    def area(self):  # public instance method
        """
        compute area of square

        returns:
            area of square
        """
        return self.__size**2  # area of square is size squared
