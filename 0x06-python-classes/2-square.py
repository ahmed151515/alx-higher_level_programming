#!/usr/bin/python3
"""0. My first square solve"""


class Square:
    """0. My first square solve"""

    def __init__(self, size=0):
        self.set_size(size)

    def set_size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
