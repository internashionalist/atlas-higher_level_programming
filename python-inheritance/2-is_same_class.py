#!/usr/bin/python3
"""
Module checks if an object has a specified class
"""


def is_same_class(obj, a_class):
    """
    Compares an object's class to a specified class

    Args:
        obj (object):       object to check
        a_class (class):    class to check against

    Returns:
        True (bool):    True if object is an instance of the class
        False (bool):   False otherwise
    """
    return type(obj) is a_class
