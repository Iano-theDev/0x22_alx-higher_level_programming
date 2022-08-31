#!/usr/bin/python3
"""Contains class Mylist"""


class MyList(list):
    """subclass of list"""

    def __init__(self):
        """Initialize object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
