#!/usr/bin/python3

"""
5-text_indentation module
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after every ".", "?", and ":" character

    Args:
        text (str): text to print

    Raises:
        TypeError:  if text is not a string

    Returns:
        None
    """

    # if text is not a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # insert \n\n after . ? and :
    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")

    # print text
    print(text, end="")
