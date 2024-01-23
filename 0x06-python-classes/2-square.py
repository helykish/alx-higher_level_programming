#!/usr/bin/python3
# 0-square.py alx project
"""Entry point: defines a square """


class Square:
    """Definition of  class representing a square"""

    def __init__(self, size=0):
        """Starting point of square class
        Args:
            size: showing the total size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
