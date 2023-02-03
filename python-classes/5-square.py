#!/usr/bin/python3
"""Defines an square class"""


class Square:
    """Defines a square with its size and validates size"""
    def __init__(self, size=0):
        self.__size = size
    """Returns the area of a square"""
    def area(self):
        return self.__size ** 2
    """@property:
        Permite axceder los atributos privados como si fueran públicos"""
    @property
    def size(self):
        return self.__size
    """@size.setter:
        Permite modificar los atributos privados"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """Print a square"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print("")
