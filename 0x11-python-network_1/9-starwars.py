#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search=' + argv[1]
    req = get(url)
    val = req.json()
    print("Number of results: {}".format(val['count']))
    for key in val['results']:
        print(key['name'])
