#!/usr/bin/python3
"""Function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Escribir algo"""
    with open(filename, "w", encoding="utf-8") as f:
        json_object = json.dumps(my_obj)
        f.write(json_object)
    """other method:f.write(json.dumps(my_obj))"""
