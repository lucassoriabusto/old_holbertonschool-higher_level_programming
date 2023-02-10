#!/usr/bin/python3
"""Defines a class BaseGeometry"""

class BaseGeometry:
    """Public instance method that raises an Exception with the message"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value, which is an integer and greater than 0"""
        if type(value) != int:
            raise Exception(f"{name} must be an integer")
        if value <= 0:
            raise Exception(f"{name} must be greater than 0")
