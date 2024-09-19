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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation
        of list_objs to a file

        Attributes:
            list_objs: list of instances

        Returns:
            None
        """
        filename = cls.__name__ + ".json"  # filename is class name + .json
        json_lists = []  # list to store JSON strings
        if list_objs:  # if not empty
            for obj in list_objs:  # iterate through list
                json_lists.append(obj.to_dictionary())  # append to list
        with open(filename, "w") as f:  # open in write mode
            f.write(cls.to_json_string(json_lists))  # write to file

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of JSON string
        representation json_string

        Attributes:
            json_string: JSON string representation

        Returns:
            string representation of list of dictionaries
        """
        if json_string:  # if json_string exists and is not empty
            return json.loads(json_string)  # return list of dictionaries
        else:
            return []  # if empty or missing, return empty list
