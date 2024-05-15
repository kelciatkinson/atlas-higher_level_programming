#!/usr/bin/python3
"""this module contains print_square function"""


def print_square(size):
    """prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print("#", end="")
        print()
