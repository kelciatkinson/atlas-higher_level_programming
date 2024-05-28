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
        json_list = []
        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs is None:
                return file.write(cls.to_json_string([]))
            else:
                for object in list_objs:
                    json_list.append(object.to_dictionary())
                json_list = cls.to_json_string(json_list)
                return file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """this method returns the list of strings json_string
        of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """this method return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            object = cls(1, 2)
        else:
            object = cls(1)
        object.update(**dictionary)
        return object

    @classmethod
    def load_from_file(cls):
        """this method returns a list of instances from json file"""
        with open("{}.json".format(cls.__name__), "r") as file:
            json_string = file.read()
        dictionaries = cls.from_json_string(json_string)
        instances = []
        for dict in dictionaries:
            instance = cls.create(**dict)
            instances.append(instance)
        return instances
