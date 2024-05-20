#!/usr/bin/python3
"""This module defines the function is_same_class"""


def is_same_class(obj, a_class):
    """This function checks if an object is
    exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
