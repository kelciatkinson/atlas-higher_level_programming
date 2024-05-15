#!/usr/bin/python3
"""this module contains addition function to add a and b"""


def add_integer(a, b=98):
    """addition function for two numbers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
