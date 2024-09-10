#!/usr/bin/python3

"""
Module 8-rectangle
"""


class Rectangle:
    """
    Defines Rectangle object

    Attributes:
        width (int):    width of the rectangle
        height (int):   height of the rectangle

    Raises:
        TypeError:  if width or height is not an integer
        ValueError: if width or height is negative

    Returns:
        Area and perimeter of rectangle
        Prints rectangle using '#'
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle instance
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

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
        return 2 * (self.__width + self.__height)

    def print(self):
        """
        Prints the rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for _ in range(self.__height):
                print(str(self.print_symbol) * self.__width)

    def __str__(self):
        """
        Returns the rectangle using '#'
        """
        if self.__width > 0 and self.__height > 0:
            string = ""
            for height in range(self.__height):
                for width in range(self.__width):
                    string += str(self.print_symbol)
                if height != self.__height - 1:
                    string += "\n"
            return string
        else:
            return ""

    def __repr__(self):
        """
        Returns the representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes the rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
