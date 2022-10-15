#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    req = request.Request("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format("content"))
