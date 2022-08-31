#!/usr/bin/python3
"""Module to check if objects are of same class"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of the specifed class
    Otherwise, returns False
    """
    return (type(obj) == a_class)
