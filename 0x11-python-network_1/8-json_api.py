#!/usr/bin/python3
"""sends a POST request to the URL with a letter as a parameter"""
from requests import post
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
        req = post(
            'http://0.0.0.0:5000/search_user', {'q': q})
        try:
            val = req.json()
            if val:
                print("[{}] {}".format(val.get('id'), val.get('name')))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
    else:
        print("No result")
