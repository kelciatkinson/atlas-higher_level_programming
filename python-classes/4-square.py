#!/usr/bin/python3
"""This module contains a class called Square."""


class Square:
    """This class defines a Square.

    Attributes:
        size (int): private instance attribute representation of Square.
    """
    def __init__(self, size=0):
        self.size = size
        """Initializes an instance of Square with a given size.
        The given size must be a non-negative integer
        or the appropriate error will be raised.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """accesses and returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size attribute to the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the public instance method area,
        that is the current square area"""
        return self.__size * self.__size
