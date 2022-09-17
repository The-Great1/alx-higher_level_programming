#!/usr/bin/python3
"""A class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """This initialises the class"""
        super().__init__(size, size, x, y, id)
        self.__size = self.width

    @property
    def size(self):
        """This retrieves the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """This returns the print function"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """This assigns values to the class attributes"""
        attr = ["id", "size", "x", "y"]
        n = 0
        if args is not None and len(args) > 0:
            for val in args:
                if n < 4:
                    setattr(self, attr[n], val)
                    n += 1

        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This returns the dictionary representation of a Square"""
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            })
