#!/usr/bin/python3
"""
Module for write_file
"""


def write_file(filename="", text=""):
    """
    method writes string to a UTF-8 text file
    and returns number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
