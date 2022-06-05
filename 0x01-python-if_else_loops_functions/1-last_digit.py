#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dig = number % 10 * -1
else:
    last_dig = number % 10
msg = (f"Last digit of {number:d} is {last_dig:d} ")
if last_dig > 5:
    print(msg + "and is greater than 5")
elif last_dig == 0:
    print(msg + "and is 0")
else:
    print(msg + "and is less than 6 and is not 0")
