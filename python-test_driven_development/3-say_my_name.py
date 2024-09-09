#!/usr/bin/python3

"""
3-say_my_name module
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints "My name is <first_name> <last_name>" using two strings

    Args:
        first_name (str):   first name
        last_name (str):    last name - default is ""

    Raises:
        TypeError:  if first_name or last_name are not strings

    Returns:
        None
    """
    # if first_name is not a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # if last_name is not a string (optional I guess)
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # print concatenated string
    print("My name is {} {}".format(first_name, last_name))
