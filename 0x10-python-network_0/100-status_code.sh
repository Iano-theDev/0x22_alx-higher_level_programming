#!/bin/bash
# sends a request to a URL passed as an argument and displays the only status code of the response
curl -sI "$1" | grep HTTP | cut -d " " -f 2
