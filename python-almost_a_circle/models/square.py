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

    def update(self, *args, **kwargs):
        """this method assigns an argument to each attribute"""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """this methos returns a dictionary representation of attributes"""
        attributes = ["id", "size", "x", "y"]
        if all(type(object) is str for object in attributes):
            return {attr: getattr(self, attr)
                    for attr in attributes if hasattr(self, attr)}
        return self.__dict__
