#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a
    parameter
"""

import requests
from sys import argv


if __name__ == "__main__":
    q_val = "" if len(argv) == 1 else argv[1]
    values = {
        'q': q_val
    }
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=values)
    try:
        json = res.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
