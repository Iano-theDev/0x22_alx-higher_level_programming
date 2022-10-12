#!/bin/bash
# sends a JSON POST request to a URL and displays the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
