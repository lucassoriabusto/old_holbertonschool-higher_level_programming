#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Defines a class Scuare that inherits the methods
    and properties of class Rectangl"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Scuare] {}/{}".format(self.__size, self.__size))
