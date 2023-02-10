#!/usr/bin/python3
"""Inherits from the BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a class Rectangle that inherits the methods
    and properties of class BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height 

        self.integer_validator("width", width)
        self.integer_validator("height", height)
