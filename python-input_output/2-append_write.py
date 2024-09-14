#!/usr/bin/python3
"""
Module for append_write
"""


def append_write(filename="", text=""):
    """
    Method appends string to a UTF-8 text file
    and returns number of characters added

    Args:
        filename (str): file to append to
        text (str): text to append to file

    Returns:
        int: number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
