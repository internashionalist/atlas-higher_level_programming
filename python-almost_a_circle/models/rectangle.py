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
