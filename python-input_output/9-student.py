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

    def to_json(self):
        """
        Method returns dictionary of Student object

        Returns:
            dict: dictionary of Student object
        """
        return self.__dict__
