#!/usr/bin/python3
"""8-class_to_json.py - class_to_join
"""


def class_to_json(obj):
    """returns the dictionary description with simple DSA
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
