#!/usr/bin/python3
"""
Module that defines a class Rectangle
"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method area.
        Returns the area of a given rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Public instance method perimeter.
        Returns the perimeter of a given rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """returns a printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += '\n'.join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """
        Return official string representation of the rectangle
        (for reproduction)
        """
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)
