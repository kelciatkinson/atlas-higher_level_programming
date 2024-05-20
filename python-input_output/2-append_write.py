#!/usr/bin/python3
"""This module defines a function that appends a file"""


def append_write(filename="", text=""):
    """This function writes a file and appends the
    contents of the file if it already exists"""
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
