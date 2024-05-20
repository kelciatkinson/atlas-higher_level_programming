#!/usr/bin/python3
"""This module defines the function is_same_class"""


def is_same_class(obj, a_class):
    """This function checks if an object is
    exactly an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
