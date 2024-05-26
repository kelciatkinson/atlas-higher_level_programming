#!/usr/bin/python3
"""Documentation will be ammended"""
from models.base import Base


class Rectangle(Base):
    """Documentation will be ammended"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Documentation will be ammended"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # calling the getter and setter methods

    @property
    # getter method
    def width(self):
        return self.__width

    @width.setter
    # setter method
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """this method returns the area of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """this method prints the Rectangle instance with the character #"""
        for i in range(self.height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height:
                print()
