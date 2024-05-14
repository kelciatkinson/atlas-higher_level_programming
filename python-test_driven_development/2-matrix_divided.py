#!/usr/bin/python3
"""this module contains division function"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division bt zero")
    new_matrix = [[round(int/div, 2) for int in list] for list in matrix]
    return new_matrix
