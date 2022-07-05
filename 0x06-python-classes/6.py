#!/usr/bin/python3
'''Defines a class Square'''


class Square:
    '''Represents a square

    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of the square in 2D plane
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize the square

        Args:
            size (int): size of the square
            position (tuple): positio of the square in 2D plane

        Returns:
            None
        '''
        self.size = size
        self.position = position

    def area(self):
        '''calculates the area of the square

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
            value (int): size of the square
        
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
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        '''getter of __position

        Returns:
            The position of the square in 2D plane
        '''
        return self.__position
    
    @position.setter
    def position(self, value):
        '''setter of __position

        Args:
            value (tupule): position of the square in 2D plane

        Return:
            None
        '''
        if type(value) is not tuple or len(value) != 2 or type(value) is not int or value[0] < 0 or type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value