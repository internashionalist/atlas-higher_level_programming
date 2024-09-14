#!/usr/bin/python3
"""
Module checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Uses isinstance() to check if an object is an instance of a class

    Args:
        obj (object):       object to check
        a_class (class):    class to check against

    Returns:
        True (bool):    True if object is an instance of the class
        False (bool):   False otherwise

    """
    return isinstance(obj, a_class)
