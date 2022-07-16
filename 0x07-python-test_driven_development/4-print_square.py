#!/usr/bin/python3
'''Contains print_square module'''


def print_square(size):
    '''
    prints a square with the character #

    takes only one parameter, (size)

    (size) is the length of the square
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
