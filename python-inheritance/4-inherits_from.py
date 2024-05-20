#!/usr/bin/python3
"""This module defines the inherits_from function"""


def inherits_from(obj, a_class):
    """This function returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False"""
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
