#!/usr/bin/python3
"""Defines a Base class"""


import json


class Base:
    """Private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """d"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """dddddddddddddddddddddddddd"""
        if list_objs is None:
            new_list = []
        else:
            """new_list = [lists.to_dictionary() for lists in list_objs]
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))"""
            
            filename = cls.__name__ + ".json" 
        with open(filename, "w", encoding="utf-8") as f:
            new_list = [lists.to_dictionary() for lists in list_objs]
            f.write(cls.to_json_string(new_list))
