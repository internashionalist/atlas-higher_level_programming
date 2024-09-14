#!/usr/bin/python3
"""
Module defines a class BaseGeometry
"""


class BaseGeometry:
    """
    Prototype for BaseGeometry class
    """

    def area(self):
        """
        TBD area method

        Raises:
            Exception: area() is not implemented

        Returns
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if value is integer and greater than 0

        Args:
            name (str): name of value
            value (int): value to check

        Raises:
            TypeError: value is not an integer
            ValueError: value is less than or equal to 0

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
