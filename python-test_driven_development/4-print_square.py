#!/usr/bin/python3

"""
4-print_square module
"""


def print_square(size):
    """
    Prints a square of size x size with the character #

    Args:
        size (int): size of the printed square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is negative

    Returns:
        None
    """
    # if size is not an int
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # if size is negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # print square
    for i in range(size):
        print("#" * size)
