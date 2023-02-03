#!/usr/bin/python3
"""Defines an empty class"""


class Square:
    """The case is defined as square"""
    pass

    def __init__(self, size=0):

        """__init__:
            the method for initializing the attributes of the class

            type:
            it returns the type of the object

            raise:
            generates exceptions and provides the name
            of the error/exception"""
        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
