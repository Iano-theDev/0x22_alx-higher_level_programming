#!/usr/bin/python3
def safe_print_integer(value):
    is_an_int = True
    try:
        int(value)
    except ValueError:
        is_an_int = False
    else:
        True
