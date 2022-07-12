#!/usr/bin/python3
'''Contains Mylist class'''


class MyList(list):
    '''a subclass of list'''
    def __init__(self):
        '''initialize the object'''
        super().__init__()
    
    def print_sorted(self):
        '''prints the sorted list'''
        