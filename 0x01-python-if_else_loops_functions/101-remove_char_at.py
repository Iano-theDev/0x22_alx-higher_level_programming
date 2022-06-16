#!/usr/bin/python3
def remove_char_at(str, n):
    return (str[:n] + str[(n if n < 0 else n + 1):])
