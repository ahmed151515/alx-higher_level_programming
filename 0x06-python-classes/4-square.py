#!/usr/bin/python3
"""0. My first square solve"""


class Square:
    """0. My first square solve"""

    def __init__(self, size=0):
        """__init__ method"""
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get area"""
        return self.__size ** 2
