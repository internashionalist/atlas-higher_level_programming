#!/usr/bin/python3

"""
this module defines a geometric class Square.
"""


class Square:
    """
    class represents a square.

    attributes:
        size (int): length of the sides of the square
        position (tuple): position of the square when printed
    """

    def __init__(self, size=0, position=(0, 0)):  # public instance method
        """
        initialize new instance of Square

        args:
            size (int): length of the sides of the square
            position (tuple): tuple of 2 integers - position of the square

        raises:
            TypeError: if size not an integer or position not tuple of 2 integers
            ValueError: if size is negative or position has negative values
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        method to get size of the square

        returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of square

        args:
            value (int): new size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is negative
        """
        if not isinstance(value, int):  # check if size is not an integer
            raise TypeError("size must be an integer")
        elif value < 0:  # check if size is negative
            raise ValueError("size must be >= 0")
        self.__size = value  # assign size to instance

    @property
    def position(self):
        """
        get the position of the square

        returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the position of the square

        args:
            value (tuple): tuple of 2 integers

        raises:
            TypeError: if position is not a tuple of 2 integers
        """
        if (not isinstance(value, tuple) or  # tuple check
                not all(isinstance(i, int) for i in value) or  # int check
                not all(i >= 0 for i in value) or  # positive check
                len(value) != 2):  # length check
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # assign position to instance

    def area(self):
        """
        compute area of square

        returns:
            int: area of square
        """
        return self.__size**2  # size squared

    def my_print(self):
        """
        prints instance of square using "#" character(s)
        """
        if self.__size == 0:
            print()  # print newline if size is 0
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
