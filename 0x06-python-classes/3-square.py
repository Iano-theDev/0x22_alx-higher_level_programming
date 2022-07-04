#!/usr/bin/python3
'''Defines a class square'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0):
        '''Initialize the square

        Args:
            size(int): size of one side of the square
        Return:
            None'''

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Calculates the area of a square

        Return:
            area of a square'''

        return(self.__size*self.__size)
