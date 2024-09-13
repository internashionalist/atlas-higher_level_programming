#!/usr/bin/python3
"""
Module for: lookup
"""


def lookup(obj):
    """
    Returns list of an object's attributes and methods

    Args:
        obj (object): object to lookup

    Returns:
        list: list of an object's attributes and methods
    """
    return dir(obj)
