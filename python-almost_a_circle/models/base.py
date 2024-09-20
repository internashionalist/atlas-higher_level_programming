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
        if list_objs is None or list_objs == []:  # if empty or None
            json_string = "[]"  # set JSON string to empty list
        else:  # if list_objs exists and is not empty
            json_string = cls.to_json_string(  # get JSON string
                [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as f:  # open file in write mode
            f.write(json_string)  # write JSON string to file

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

    @classmethod
    def create(cls, **dictionary):
        """
        This method creates an instance with all attributes set.

        Attributes:
            dictionary: key/value pairs of attributes

        Returns:
            dummy_inst: new instance with attributes set
        """
        if cls.__name__ == "Rectangle":  # if Rectangle
            dummy_inst = cls(1, 1)  # create dummy - default 1x1
        if cls.__name__ == "Square":  # if Square
            dummy_inst = cls(1)  # create dummy - default 1x1
        dummy_inst.update(**dictionary)  # update w dict attributes
        return dummy_inst  # return new instance

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances from a file

        Returns:
            inst_list: list of instances
        """
        filename = cls.__name__ + ".json"  # class name + .json
        inst_list = []  # list to store instances (empty for now)
        if os.path.exists(filename):  # if file exists
            with open(filename, "r") as f:  # open in read mode
                json_lists = cls.from_json_string(f.read())  # read JSON string
            for json_dict in json_lists:  # iterate through list
                inst_list.append(cls.create(**json_dict))  # append instances
        return inst_list  # return list of instances (empty if no file)
