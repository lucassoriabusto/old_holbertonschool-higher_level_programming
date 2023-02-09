#!/usr/bin/python3
"""Check if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """true if it is exact same object"""
    if type(obj) is a_class:
        return True
    else:
        return False
