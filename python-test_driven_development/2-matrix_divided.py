#!/usr/bin/python3

"""
2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    Function divides all elements of a matrix by a number (div)

    Args:
        matrix (list):      list of lists of ints/floats
        div (int/float):    number by which to divide all elements

    Raises:
        TypeError:  if matrix is not a list of lists of ints/floats,
                    if rows are unequal, or if div is not an int/float
        ZeroDivisionError:  if div is 0

    Returns:
        list:   new matrix with all elements divided by div
    """

    # if matrix is not a list of lists of ints/floats
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, (int, float)) for row in matrix
                for element in row)):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    # if rows are not of equal length
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # if div is not an int/float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # return brand new matrix with all elements divided (2 dec places)
    return [[round(element / div, 2) for element in row] for row in matrix]
