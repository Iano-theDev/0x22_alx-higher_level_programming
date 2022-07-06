#!/usr/bin/python3
'''
Module for write_file function
'''


def write_file(filename="", text=""):
    '''Writes a string to a file (UTF8) and returns

     number of characters written
     '''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
