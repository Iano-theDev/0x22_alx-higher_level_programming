#!/usr/bin/python3
"""Post an email to a URL and displays the body of the response"""


if __name__ == "__main__":
    import requests
    from sys import argv
    email = {'email': argv[2]}
    r = requests.post(argv[1], params=email)
    text = r.text
    print("{}".format(text))
