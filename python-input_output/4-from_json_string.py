#!/usr/bin/python3
"""Function that returns an object (Python data structure)
represented by a JSON string"""


import json


def from_json_string(my_str):
    """json loads():
    returns a Python dictionary object from a JSON-formatted string"""
    return json.loads(my_str)
