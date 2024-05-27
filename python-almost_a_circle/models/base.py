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

    @staticmethod
    def to_json_string(list_dictionaries):
        """this method returns JSON string representation
        of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this method writes the JSON string representation
        of list_objs to a file"""
        json_str = []
        if list_objs is not None:
            with open("{}.json".format(cls.__name__), "w") as file:
                for object in list_objs:
                    json_str.append(object.to_dictionary())
                json_str = cls.to_json_string(json_str)
                return file.write(json_str)
        else:
            return []
