#!/usr/bin/python3
lower = True
ord_a = ord('a')
ord_A = ord('A')
for c in range(122, 96, -1):
    print("{:c}".format(c if lower else ord_A + c - ord_a), end="")
    lower = (not lower)
