#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """Creates an object"""
    with open(filename, encoding="utf-8") as f:
        json_object = f.read()
        return json.loads(json_object)
