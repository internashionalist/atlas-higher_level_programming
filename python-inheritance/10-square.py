#!/usr/bin/python3
"""
Module defines a child class Square that inherits 9-rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Prototype for Square class
    """
    def __init__(self, size):
        """
        Initializes a Square object that inherits 9-rectangle

        Arguments:
            size (int): size of square

        Methods:
            integer_validator:  inherited
            area:               inherited

        Returns:
            None
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates area of square

        Returns:
            Area of square
        """
        return self.__size ** 2