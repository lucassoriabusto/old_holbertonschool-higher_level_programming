#!/usr/bin/python3
"""Checks whether it is an instance or an instance of an inherited class"""


def is_kind_of_class(obj, a_class):
    """isinstance:
    Returns True if the specified object is of the specified type,
    otherwise False
    """
    return isinstance(obj, a_class)
