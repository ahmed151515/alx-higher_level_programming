#!/usr/bin/python3
"""0. My first square solve"""


class Square:
    """0. My first square solve"""

    def __init__(self, size=0):
        """__init__ method"""
        self.set_size(size)

    def set_size(self, size):
        """setter method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """get area"""

        return self.__size ** 2
