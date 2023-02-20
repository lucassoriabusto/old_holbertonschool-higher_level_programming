#!/usr/bin/python3
"""Defines a Base class"""


import json
from os import path


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
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            new_list = []
        else:
            new_list = [lists.to_dictionary() for lists in list_objs]
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            json_string = cls.to_json_string(new_list)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if path.exists(f"{cls.__name__}.json") is None:
            return []
        with open(f"{cls.__name__}.json", encoding='utf-8') as f:
            lists_inst = []

            for d in cls.from_json_string(f.read()):
                lists_inst.append(cls.create(**d))
        return lists_inst

