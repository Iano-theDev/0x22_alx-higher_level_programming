#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        letter = ord(str[c])
        if ord('a') <= letter <= ord('z'):
            letter -= 32
        print("{}".format(chr(letter)), end='')
    print()

