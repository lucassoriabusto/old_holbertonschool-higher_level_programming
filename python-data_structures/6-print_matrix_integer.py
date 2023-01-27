#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i in n:
            if n != i:
                print("{:d}".format(i), end="")
                print(" ", end="")
        print()
