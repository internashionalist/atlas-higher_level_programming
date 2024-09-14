#!/usr/bin/python3
"""
Module for save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method writes an object to a text file using JSON representation

    Args:
        my_obj (object): object to write to file
        filename (str): name of file to write to

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
