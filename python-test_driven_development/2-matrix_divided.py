#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    for n in (matrix):
        for i in n:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix 
                        (list of lists) of integers/floats")
    """Each row of the matrix must be of the same size"""
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    """"""
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    """"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """function that divides a matrix and rounded to 2 decimal places"""
    new_matrix = []
    for n in matrix:
        for i in n:
            new_matrix.append(round(i / div, 2))
    return new_matrix
