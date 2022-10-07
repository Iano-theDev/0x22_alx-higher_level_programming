#!/bin/bash
# script takes in a url and sends a request to that url 
# displays the size of the body of the response

curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
