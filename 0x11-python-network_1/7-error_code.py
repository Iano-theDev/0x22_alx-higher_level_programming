#!/usr/bin/python3
"""Takes in a URL sends a request to the URL and
displays the body of the response"""


if __name__ == "__main__":
    import requests
    from sys import argv
    try:
        requests.get(argv[1])
    except requests.exceptions.HTTPError as e:
        print("Error code {}".format(e.response.text))
