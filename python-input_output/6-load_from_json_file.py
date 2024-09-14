#!/usr/bin/python3
"""
Module for load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Function creates an object from a JSON file

    Args:
        filename (str): file from which to extract object

    Returns:
        object: object represented by the JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
