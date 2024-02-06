#!/usr/bin/python3
""" File that returns dictionary descript with a simple
data structure for a JSON serialization of an obj
"""


def class_to_json(obj):
    """ Func that retuns the dictionary descript of an object """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
