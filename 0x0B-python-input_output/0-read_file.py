#!/usr/bin/python3
'''
Contains the read_file function
'''


def read_file(filename=""):
    '''reads a text file in utf-8 encoding and prints to stdout'''
    with open(filename,'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
