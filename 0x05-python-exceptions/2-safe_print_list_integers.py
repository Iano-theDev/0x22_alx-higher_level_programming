#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            new_list += 1
        except (ValueError, TypeError):
            continue
    print()
    return new_list