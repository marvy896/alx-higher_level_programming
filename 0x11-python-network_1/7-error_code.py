#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from requests import get
from sys import argv


if __name__ == '__main__':
    req = get(argv[1])
    if (req.status_code == 200):
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
