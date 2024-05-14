#!/usr/bin/python3
"""defines a new class called Square"""


class Square:
    """defines a Square"""
    def __init__(self, size=0):
        self.size = size
        """private instance attribute size"""
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

    def my_print(self):
        """prints a square made of # with x number of
        rows and columns determined by the size attribute"""
        if self.__size == 0:
            print()
        for i in range(1, self.__size + 1):
            for j in range(1, self.__size + 1):
                print("#", end="")
            print()
