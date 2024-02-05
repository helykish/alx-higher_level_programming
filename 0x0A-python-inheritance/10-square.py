#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """func Represent a square."""

    def __init__(self, size):
        """Initial a new square.

        Args:
            size (int): The area of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
