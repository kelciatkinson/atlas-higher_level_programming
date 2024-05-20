#!/usr/bin/python3
import json
"""This module defines the to_json_string function"""


def to_json_string(my_obj):
    """This function returns the JSON representation
    of an object as a string"""
    return json.dumps(my_obj)
