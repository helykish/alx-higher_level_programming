#!/usr/bin/python3
""" File contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """ Func that writes to a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
