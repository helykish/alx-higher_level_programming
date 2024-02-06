#!/usr/bin/python3
""" File contains a func that reads from a file """


def read_file(filename=""):
    """ Func reads frm a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
