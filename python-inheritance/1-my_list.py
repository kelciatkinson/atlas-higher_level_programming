#!/usr/bin/python3
"""This module contains the class MyList and inherits from list"""


class MyList(list):
    def __init__(self):
        """instance of MyList"""
        super().__init__()

    def print_sorted(self): 
        """sorts and prints a given list"""
        return list.sort(self)
