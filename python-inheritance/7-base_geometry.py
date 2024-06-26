#!/usr/bin/python3
"""This module defines the BaseGeometry Class"""


class BaseGeometry():
    """initializes BaseGeometry"""
    def area(self):
        """This function raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
