#!/usr/bin/python3
"""Defines an square class"""


class Square:
    """Defines a square with its size and validates size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        """Comprueba si los valore de la tupla posición son validos"""
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.__position[0]) != int or type(self.__position[1]) != int:
             raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
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
    """Prints a square at a given position"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for p in range(self.__position[1]):
                    print("")
            for x in range(self.__size):
                for z in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
    
    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, value):

        """if type(self.__position) != tuple or type(value) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value"""

    """@position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int or len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position"""
