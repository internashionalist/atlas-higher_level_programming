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
            width (int):    width of rectangle
            height (int):   height of rectangle

        Methods:
            integer_validator:  from 7-base_geometry
            area:               from 7-base_geometry

        Returns:
            None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
