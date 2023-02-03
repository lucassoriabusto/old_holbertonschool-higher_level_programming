#!/usr/bin/python3
"""Defines an empty class"""


class Square:
    pass

    def __init__(self, size=0):
        """ Write a class Square that defines a square
            as private instance attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
