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

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age

        
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method returns dictionary of Student object

        Args:
            attrs (list): list of attributes to return

        Returns:
            dict: dictionary of Student object
        """
        if attrs is None:  # if no attributes specified, return all
            return self.__dict__

