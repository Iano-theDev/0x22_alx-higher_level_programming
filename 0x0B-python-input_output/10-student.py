#!/usr/bin/python3
'''
contains class student
'''


class Student:
    def __init__(self, first_name, last_name, age):
        '''initializes the student class'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        returns a dictionary representation of a student
        instance with specified attributes
        '''
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except TypeError:
                pass
        return new_dict
