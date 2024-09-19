#!/usr/bin/python3
"""
This module contains the Square class.
    - Square inherits from Rectangle
    - Rectangle inherits from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle and Base

    Methods:
        __init__: initializes instance of Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instance of Square class

        Attributes:
            size(int): size of square
            x(int): x coordinate of square
            y(int): y coordinate of square
            id(int): specified or inherited from Base counter
        """
        super().__init__(size, size, x, y, id)  # calling __init__ of Rectangle
        self.size = size

    def __str__(self):  # overriding __str__ method
        """
        This method overrides the __str__ method to return a string

        Returns:
            stringSqr: string representation of Square
        """
        stringSqr = f"[Square] ({self.id})"
        stringSqr += f" {self.x}/{self.y} - {self.size}"
        return stringSqr

    @property  # getter for size
    def size(self):
        return self.width

    @size.setter  # setter for size
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        This method updates the attributes of the Square

        Attributes:
            *args: list of arguments
                0: id
                1: size
                2: x
                3: y
            **kwargs: key/value pairs of attributes
        """
        attributes = ["id", "size", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of Square.

        Returns:
            dictionary: dictionary representation of Square
        """
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict
