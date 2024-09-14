#!/usr/bin/python3
"""
Module checks if an object clas is a subclass of a specified class
"""


def inherits_from(obj, a_class):
    """
    Uses issubclass() method

    Args:
        obj (object):       object to check
        a_class (class):    class to check against

    Returns:
        True (bool):    True if object is an instance of the class
        False (bool):   False otherwise

    """
    return issubclass(type(obj), a_class)
