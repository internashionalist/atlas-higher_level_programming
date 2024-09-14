#!/usr/bin/python3
"""
Module for student
"""


class Student:
    """
    Class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object

        Attributes:
            first_name (str):   first name
            last_name (str):    last name
            age (int):          age

        Methods:
            to_json:            returns dictionary of attributes
            reload_from_json:   replaces all attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method returns dictionary of Student object

        Attributes:
            attrs (list): list of attributes to return

        Returns:
            dict: dictionary of Student object
        """
        if attrs is None:  # if no attributes specified, return all
            return self.__dict__
        else:
            new_dict = {}  # create new dictionary
            for key, value in self.__dict__.items():  # iterate through dict
                if key in attrs:  # if key in attrs
                    new_dict[key] = value  # add to new_dict
            return new_dict  # return new_dict

    def reload_from_json(self, json):
        """
        Method replaces all attributes of Student

        Attributes:
            json (dict): dictionary of attributes used to replace

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
