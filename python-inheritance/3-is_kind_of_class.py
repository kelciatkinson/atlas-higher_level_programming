#!/usr/bin/python3
"""This module defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """This function returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
