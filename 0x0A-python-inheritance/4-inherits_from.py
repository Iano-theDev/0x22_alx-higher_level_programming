#!/usr/bin/python3
"""contains inherits_from class"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that
    inherits directly or indirectly from the specified class,
    otherwise, returns False"""

    return(issubclass(type(obj), a_class) and type(obj) != a_class)
