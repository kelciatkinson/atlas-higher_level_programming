#!/usr/bin/python3
"""This module contains the class MyList"""


class MyList(list):
    """This class inherits from list"""
    def __init__(self):
        """instance of MyList"""
        super().__init__()

    def print_sorted(self):
        """sorts and prints a given list"""
        print(sorted(self))
