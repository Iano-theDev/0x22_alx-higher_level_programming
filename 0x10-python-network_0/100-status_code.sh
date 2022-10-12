#!/bin/bash
# sends a request to a URL passed as an argument and displays the only status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
