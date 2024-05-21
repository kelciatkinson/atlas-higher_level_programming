#!/usr/bin/python3
"""This module defines the class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class creates a new object Square"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
