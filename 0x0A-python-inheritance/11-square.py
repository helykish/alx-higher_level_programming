#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created Mon Feb 06 2024

@creator: Francis
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    A Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        Init func for Square

        Attributes:
            size (int): The area of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str func that print with/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A func that calc the size of the Square
        """
        return self.__size ** 2
