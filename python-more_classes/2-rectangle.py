#!/usr/bin/python3

"""
Module 2-rectangle
"""


class Rectangle:
    """
    Defines Rectangle object
    """

    def __init__(self, width=0, height=0):
        """
        Initializes  rectangle with given width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of Rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of Rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
