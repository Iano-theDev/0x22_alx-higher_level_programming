#!/bin/bash
# takes in a URL, sends a post request to the passed URL and displays the body of the response
curl -o -sX  POST -H {"email:test@gmail.com", "subject:I will always be here for PLD"} "$1"
