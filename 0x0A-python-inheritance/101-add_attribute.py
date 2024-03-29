#!/usr/bin/python3
"""func that add new attribute to an object
if successful
"""


def add_attribute(obj, attribute, value):
    """dds a new attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
