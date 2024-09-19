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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON representation of list_dictionaries

        Attributes:
            list_dictionaries: list of dictionaries

        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)  # return JSON string
        else:
            return "[]"  # if empty or missing, return empty list
