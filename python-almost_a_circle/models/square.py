#!/usr/bin/python3
"""Documentation will be ammended"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Documentation will be ammended"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size)
