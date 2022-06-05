#!/usr/bin/python3
import random 
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is greater than Zero")
elif number < 0:
    print(f"{number:d} is less than  zero")
else:
    print(f"{number:d} is zero")

