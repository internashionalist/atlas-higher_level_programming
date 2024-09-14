#!/usr/bin/python3
"""
Module defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Prototype for Rectangle class
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object

        Arguments:
            width (int):    width of rectangle - default 0
            height (int):   height of rectangle - default 0

        Methods:
            integer_validator:  inherited - 7-base_geometry
                                validates value is integer and > 0
            area:               inherited - 7-base_geometry
                                calculates area of rectangle
        Returns:
            None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates area of rectangle

        Returns:
            Area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Uses __str__ for string representation of rectangle

        Returns:
            Representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
