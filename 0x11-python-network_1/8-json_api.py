#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


if __name__ == "__main__":
    from sys import argv
    import requests
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    post_req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        post_req_data = post_req.json()
        id = post_req_data.get('id')
        name = post_req_data.get('name')
        if len(post_req_data) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
