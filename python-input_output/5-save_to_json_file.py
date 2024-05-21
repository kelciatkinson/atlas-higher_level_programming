#!/usr/bin/python3
"""This module defines the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text
    file, using a JSON representation"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
