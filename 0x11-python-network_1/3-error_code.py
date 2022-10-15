#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body
of the respponse decoded in utf-8
"""


if __name__ == "__main__":
    from sys import argv
    import urllib.error as error
    import urllib.request as request
    req = request.Reuest(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
        exept error.HTTPError as e:
            print("Error code: {}".format(e.code))
