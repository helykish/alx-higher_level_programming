#!/usr/bin/python3
""" File contains a func that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Func returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: when str cannot be decoded

    """
    return json.loads(my_str)
