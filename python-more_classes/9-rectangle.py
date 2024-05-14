#!/usr/bin/python3
"""defines a new class called Rectangle"""


class Rectangle:
    """does nothing yet, code will be wrriten later"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        """private instance attribute width"""
        self.__height = height
        """private instance attribute height"""
        Rectangle.number_of_instances += 1

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
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """returns a rectangle made of # with x number of
        rows and columns determined by the width/height attribute"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(1, self.__height + 1):
            for j in range(1, self.__width + 1):
                rect += self.print_symbol
            if i != self.__height:
                rect += "\n"
        return rect

    def __repr__(self):
        """returns a string that describes the pointer
        of the rectangle by default"""
        return "{}({}, {})".format(type(self).__name__,
                                   self.__width, self.__height)

    def __del__(self):
        """prints message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
