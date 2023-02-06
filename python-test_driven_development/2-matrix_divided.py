#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    new_matrix = []
    for n in (matrix):
        for i in n:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    
    for n in matrix:
        new_matrix.append(list(map(lambda x: x / div, n)))

    return new_matrix
