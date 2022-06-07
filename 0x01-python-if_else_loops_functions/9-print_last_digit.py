#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return(print("{:d}".format(number % -10, end='')))
    else:
        return(print("{:d}".format(number % 10, end='')))
