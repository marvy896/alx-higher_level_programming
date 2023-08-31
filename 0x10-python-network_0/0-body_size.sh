#!/bin/bash
# takes in a URL, sends a request and displays the size of the body of the response
curl -s $1 | wc -c
