#!/usr/bin/python3
"""defines a new class called Rectangle"""


class Rectangle:
    """initializes Rectangle"""
    def __init__(self, width=0, height=0):
        """initializes Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """accesses and returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute to the value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """accesses and returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute to the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the public instance method area,
        that is the current rectangle area"""
        return self.__width * self.__height
    
    def perimeter(self):
        """returns the public instance method perimeter,
        that is the current rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
