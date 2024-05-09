#!/usr/bin/python3
"""defines a new class called Square"""


class Square:
    """defines a Square"""
    def __init__(self, size=0):
        self.__size = size
        """private instance attribute size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the public instance method area, that is the current square area"""
        self.area = self.__size * self.__size
        return (self.area)
