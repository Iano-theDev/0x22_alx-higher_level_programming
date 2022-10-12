#!/bin/bash
# sends a JSON POST request to a URL and displays the response
curl -sX POST "$1" -f "$2"
