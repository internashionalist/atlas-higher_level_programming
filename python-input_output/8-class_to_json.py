#!/usr/bin/python3
"""
Module for class_to_json
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (object): object to serialize

    Returns:
        dict: dictionary representation of object
    """
    return obj.__dict__  # is it that simple?
