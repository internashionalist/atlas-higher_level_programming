#!/usr/bin/python3
"""
Module for to_json_string
"""
import json


def to_json_string(my_obj):
    """
    Method returns JSON representation of an object

    Args:
        my_obj (object): object to convert to JSON

    Returns:
        str: JSON representation of object
    """
    return json.dumps(my_obj)  # "dumps" FTW
