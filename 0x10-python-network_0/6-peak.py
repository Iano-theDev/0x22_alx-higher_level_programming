#!/usr/bin/python3
"""Contains function to find peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    li = list_of_integers
    len_li = len(li)
    if len_li == 0:
        return
    m = len_li // 2
    if (m == len_li - 1 or li[m] >= li[m + 1]) and\
            (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != len_li - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
