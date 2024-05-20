#!/usr/bin/python3
"""This module defines a function that writes a file"""


def write_file(filename="", text=""):
    """This function writes a file and overwrites the
    contents of the file if it already exists"""
    with open(filename, "w") as f:
        f.write(text)
        return len(text)
