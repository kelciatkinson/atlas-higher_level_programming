#!/usr/bin/python3
"""This module defines the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text
    file, using a JSON representation"""
    try:
        with open(filename, "w") as file:
            json.dump(my_obj, file)
    except Exception as e:
        print("Error: {}".format(e))

