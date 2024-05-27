#!/usr/bin/python3
"""Documentation will be ammended"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Documentation will be ammended"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[{}] ({}) {}/{} - {}"
                .format(self.__class__.__name__,
                        self.id, self.x, self.y, self.width))

    # getter for size
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
