#!/usr/bin/python3
"""0. My first square solve"""


class Square:
    """0. My first square solve"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """setter method"""
        if type(value) != tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = value

    def area(self):
        """get area"""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print
            return
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
