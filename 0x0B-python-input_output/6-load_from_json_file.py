#!/usr/bin/python3
""" File that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Func creates an Object from a JSON file

    Args:
        filename: textfile name

    Raises:
        Exception: when object can not be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
