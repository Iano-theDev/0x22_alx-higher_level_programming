#!/bin/bash
# sends a delete request to URL passed a the first argument and displays the body of the response
curl -sX DELETE "$1"
