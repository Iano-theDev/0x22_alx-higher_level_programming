#!/usr/bin/python3
"""module contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the oject is an instance of a class that inherited
    from the specified class otherwise, returns False.
    """

    return (isinstance(obj, a_class))
