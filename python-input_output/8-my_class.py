#!/usr/bin/python3
"""This module defines the MyClass function"""

class MyClass:
    def __init__(self, name):
        """Instance method of MyClass"""
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
