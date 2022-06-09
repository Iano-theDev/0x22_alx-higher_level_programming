#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    prev_num = 0
    curr_num = 0
    for letter in roman_string[::-1]:
        prev_num = curr_num
        curr_num = romans[letter]
        r += (curr_num if curr_num >= prev_num else -curr_num)
    return r
