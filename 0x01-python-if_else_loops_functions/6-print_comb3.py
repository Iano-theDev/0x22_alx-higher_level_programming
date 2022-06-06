#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(1, 10):
        if num2 > num1 and num1 < 8:
            print("{:d}{:d}, ".format(num1, num2), end='')
        elif num2 > num1:
            print("{:d}{:d}".format(num1, num2))
