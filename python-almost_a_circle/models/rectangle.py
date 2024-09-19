#!/usr/bin/python3
"""
This module contains the Rectangle class
which inherits from the Base class
"""
from models.base import Base  # inheriting from base.py


class Rectangle(Base):
    """
    Rectangle class - inherits from Base

    Methods:
        __init__: initializes instance of Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes instance of Rectangle class

        Attributes:
            id(int):        specified or inherited from Base counter
            width(int):     width of rectangle
            height(int):    height of rectangle
            x(int):         x coordinate of rectangle
            y(int):         y coordinate of rectangle

        Methods:
            __init__: initializes instance of Rectangle
        """
        super().__init__(id)  # calling __init__ of Base
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property  # getter for width
    def width(self):
        return self.__width

    @width.setter  # setter for width with validation
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property  # getter for height
    def height(self):
        return self.__height
    
    @height.setter  # setter for height with validation
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property  # getter for x
    def x(self):
        return self.__x
    
    @x.setter  # setter for x with validation
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property  # getter for y
    def y(self):
        return self.__y

    @y.setter  # setter for y with validation
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value