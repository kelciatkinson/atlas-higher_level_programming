#!/usr/bin/python3
"""This module will return a list of lists representing the Pascals triangle"""


def pascal_triangle(n):
    """This function will return an empty list if n <= 0,
    or a list of lists of intgers"""
    new_list = []
    if n <= 0:
        return new_list
    for i in range(n):
        # number of rows
        row = []
        for k in range(i + 1):
            # number of items in each row
            if k == 0 or k == i:
                row.append(1)
            else:
                row.append(new_list[i - 1][k] + new_list[i - 1][k - 1])
        new_list.append(row)
    return new_list
