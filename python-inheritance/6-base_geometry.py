#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Public instance method that raises an Exception with the message"""
    def area(self):
        raise Exception("area() is not implemented")
