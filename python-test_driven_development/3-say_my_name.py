#!/usr/bin/python3
"""contains a function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """prints a string"""
    if type(first_name) is str:
        print("My name is {} {}".format(first_name, last_name))
    else:
        raise Exception("first_name must be a string")