#!/usr/bin/python3
"""This module contains a function to read files"""

def read_file(filename=""):
    """This function reads a file"""
    with open(filename, "r") as f:
        f_contents = f.read()
        print(f_contents, end="")
