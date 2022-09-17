#!/usr/bin/python3
"""The rectnagle class inherits from base"""

from models.base import Base


class Rectangle(Base):
    """This is the class definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This initialises the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This retrieves the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This retreives the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """this sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This computes the area of the rectangle"""
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        """This prints a graphical representation of the rectangle with #"""
        for r in range(self.__y):
            print()
        for n in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for m in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """This runs when print is called"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """This assigns an argument to each attribute"""
        kw = ["id", "width", "height", "x", "y"]
        n = 0

        if args is not None and len(args) > 0:
            for val in args:
                if n < 5:
                    setattr(self, kw[n], val)
                    n += 1

        elif kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """This returns the dictionary representation of a Rectangle"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            })
