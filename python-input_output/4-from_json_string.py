#!/usr/bin/python3
"""
Module for from_json_string
"""
import json


def from_json_string(my_str):
    """
    Method uses loads and returns Python object represented by JSON string

    Args:
        my_str (str): JSON string to convert to Python object

    Returns:
        object: Python object represented by JSON string
    """
    return json.loads(my_str)
