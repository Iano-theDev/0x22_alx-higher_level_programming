#!/usr/bin/python3
"""Takes in github credentials and uses the GitHub API to display your id"""


if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth
    req = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get('id'))
