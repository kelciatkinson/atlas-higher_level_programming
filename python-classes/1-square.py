#!/usr/bin/python3
"""This module contains a class called Square."""


class Square:
    """This class defines a Square.

    Attributes:
        size (int): private instance attribute representation of Square.
    """
    def __init__(self, size):
        """Initializes an instance of Square with a given size."""
        self.__size = size
