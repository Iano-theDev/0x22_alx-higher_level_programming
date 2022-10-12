#!/bin/bash
# sends a request to a URL passed as an argument and displays the only status code of the response
curl -sI curl -s -o /dev/null -I -w "%{http_code}" "$1"
