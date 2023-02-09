#!/usr/bin/python3
"""Function that returns True if the object is an
instance of a class that inherited"""


def inherits_from(obj, a_class):
    """isinstance:
    Returns True if the specified object is of the specified type,
    otherwise False
    """
    return isinstance(obj, a_class)
