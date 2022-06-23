#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        n = a / b
    except ZeroDivisionError:
        n = None
    else:
        return n
    finally:
        print("Inside result: {}".format(n))
