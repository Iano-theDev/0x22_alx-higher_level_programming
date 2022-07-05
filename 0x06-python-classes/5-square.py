#!/usr/bin/python3
'''Defines a class Square'''


class Square:
    '''Represents a square

    Attributes:
        __size (int): size of one side of the square
    '''

    def __init__(self, size=0):
        '''Initialize the square

        Args:
            size (int): size of a side of the square

        Return:
            None
        '''
        self.size = size

    def area(self):
        '''Calculates the area of the square

        Returns:
            The area of the square
        '''
        return (self.__size) ** 2

    @property
    def size(self):
        '''getter of __size

        Returns:
            The size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter of __size

        Args:
            value (int): the size of the square

        Returns:
            None
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        '''prints the square

        Returns:
            None
        '''
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
