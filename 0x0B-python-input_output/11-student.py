#!/usr/bin/python3
'''
contains Student class
'''


def __init__(self, fistname, last_name, age):
    '''initialize the student'''
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self, attrs=None):
    '''
    retuens a dictionary representation of a student instance
    with specified attributes
    '''
    if attrs is None:
        return self.__dict__
    new_dict = {}
    for a in attrs:
        try:
            new_dict[a] = self.__dict__[a]
        except Exception:
            pass
    return new_dict


    def reload_from_json(self, json):
        """Replaces all attributs of Student instance from json"""
        for key in json:
            setattr(self, key, json[key])