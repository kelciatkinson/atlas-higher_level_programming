#!/usr/bin/python3
"""Documentation will be ammended"""
import json


class Base:
    """Documentation will be ammended"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Documentation will be ammended"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """this method returns JSON string representation
        of list_dictionaries"""
        return json.dumps(list_dictionaries)
