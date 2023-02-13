#!/usr/bin/python3
"""d"""


import json




def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as f:
        json_object = f.read()
        return json.loads(json_object)
