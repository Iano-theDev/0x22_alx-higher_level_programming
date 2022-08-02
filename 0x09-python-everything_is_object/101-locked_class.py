#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
