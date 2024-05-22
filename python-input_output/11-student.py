#!/usr/bin/python3
"""This module defines the MyClass function"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initializes class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list):
            if all(type(object) is str for object in attrs):
                return {attr: getattr(self, attr)
                        for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """This function sets the value of the attribute of an object"""
        for key, value in json.items():
            setattr(self, key, value)
