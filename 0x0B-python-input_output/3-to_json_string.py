#!/usr/bin/python3
""" File contains func tht returns the JSON
representating an object
"""
import json


def to_json_string(my_obj):
    """ Func that returns the JSON representation of an object

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
