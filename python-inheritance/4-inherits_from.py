#!/usr/bin/python3
"""Function that returns True if the object is an
instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Checks if it is an object of an inherited class"""
    """issubclass: Check if a class is a subclass of another class or not"""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
