#!/usr/bin/python3
"""This module defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file"""
    with open(filename, "r") as file:
        return json.load(file)
