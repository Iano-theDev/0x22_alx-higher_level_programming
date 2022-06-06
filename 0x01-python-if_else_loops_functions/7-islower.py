#!/usr/bin/python3
def islower(c):
    for c in range(ord('a'), ord('z') + 1):
        print("{:c} is lower".format(c))
        return(True)
    else:
        print("{:c} is upper".format(c))
        return(False)
