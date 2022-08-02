#!/usr/bin/python3
class LockedClass:
    """
    Locked class that only allows the user dynamically
    create theinstance attribute 'first_name'
    """
    __slots__ = ['first_name']
