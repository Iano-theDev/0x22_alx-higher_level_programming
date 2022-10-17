#!/usr/bin/python3
"""Sends a request to a URL and displays the value
of the variable X-Requested-Id
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    my_req = requests.get(argv[1])
    print(my_req.headers.get('X-Request-Id'))
