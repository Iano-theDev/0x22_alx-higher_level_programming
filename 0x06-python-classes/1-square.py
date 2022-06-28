#!/usr/bin/python3
""" Definition of Square class"""


class Square:
    """A Square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square

        Args:
            size (int): size of a side of the sqaure

        Returns: None
        """
        self.__size = size
