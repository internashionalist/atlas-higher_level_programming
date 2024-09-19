#!/usr/bin/python3
"""
This module contains the Base class.
"""
import json
import os


class Base:
    """
    Base class for all other classes

    Attributes:
        __nb_objects: instance counter

    Methods:
        __init__: initializes instance of Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance of Base class

        Attributes:
            id: id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
