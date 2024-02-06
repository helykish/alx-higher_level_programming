#!/usr/bin/python3
""" File that writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Func writes an object to text file
    by a JSON representation

    Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when object can not encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
