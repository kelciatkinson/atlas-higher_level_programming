#!/usr/bin/python3
"""This module contains a class called Square."""


class Square:
    """This class defines a Square.

    Attributes:
        size (int): private instance attribute representation of Square.
    """
    def __init__(self, size=0):
        self.__size = size
        """Initializes an instance of Square with a given size.
        The given size must be a non-negative integer
        or the appropriate error will be raised.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size
