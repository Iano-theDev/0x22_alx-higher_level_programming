#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me causing the server to respond with a message in the body
curl -sLX PUT -H -d "You got me" 0.0.0.0:5000/catch_me