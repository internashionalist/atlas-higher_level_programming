#!/usr/bin/python3

"""
this module's function adds two integers
"""


def add_integer(a, b=98):
    """
    Function adds two ints or floats

    Args:
    a (int): first integer
    b (int): second integer - default is 98

    Raises:
    TypeError: if a or b are not integers or floats

    Returns:
    int: the sum of a and b
    """
    if isinstance(a, float):
        a = int(a)  # convert float to int
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):  # check if int
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b  # return sum of a and b
