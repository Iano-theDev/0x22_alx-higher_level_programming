#!/usr/bin/python3
'''
contains pascal_triangle function
'''


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing
    the Pascal's triangle.

    Args:
        n (int): An integer
    '''

    r = []
    prev = []
    curr = []
    curr_len = 0

    while n > 0:
        prev = curr
        curr = curr + [1]
        i = 1

        while i > 0:
            curr[i] = prev[i - 1] + prev[i]
            i += 1
        r.append(curr)
        n -= 1

    return r
