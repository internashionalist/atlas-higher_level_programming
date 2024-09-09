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

    result = ""  # string to store result
    i = 0  # iterator
    while i < len(text):  # iterate through text
        result += text[i]  # add each character to result
        if text[i] in ".?:":  # if . or ? or :
            result += "\n\n"  # add 2 new lines
            i += 1  # move to next character
            while i < len(text) and text[i] == " ":  # skip spaces
                i += 1  # move to next character
            continue
        i += 1 # move to next character

    print(result, end="")  # print resulting text and pray
