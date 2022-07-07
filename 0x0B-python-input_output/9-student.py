#!/usr/bin/python3
'''
contains thr class "Student"
'''


class Student:
    def __init__(self, first_name, last_name, age):
        '''initializes thr student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns a dictionary representation of a Student instance'''
        return self.__dict__
