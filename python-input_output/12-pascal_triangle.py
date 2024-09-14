#!/usr/bin/python3
"""
Module for pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a matrix representing a 'Pascal’s Triangle' of n size
    """
    if n <= 0:
        return []

    Pascals = [[1]]  # first row is always [1]
    if n > 1:
        Pascals.append([1, 1])  # second row is always [1, 1]
        for i in range(2, n):  # now it gets fun
            row = [1]  # first element
            for k in range(1, i):  # middle elements - sum of two above
                row.append(Pascals[i - 1][k - 1] + Pascals[i - 1][k])
            row.append(1)  # last element
            Pascals.append(row)  # add completed row
    return Pascals  # return Pascals Triangle!
