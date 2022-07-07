#!/usr/bin/python3
"""``pascal_triangle`` module"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing the Pascal's triangle
        of n.
            Args:
                n (int): An integer
    """
    r = []
    prev = []
    curr = []
    curr_len = 0

    while n > 0:
        prev = curr
        curr = curr + [1]
        i = 1
        while i < len(prev):
            curr[i] = prev[i - 1] + prev[i]
            i += 1
        r.append(curr)
        n -= 1

    return r
