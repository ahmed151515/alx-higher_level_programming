#!/usr/bin/python3
"""solve task 0x08. Python - More Classes and Objects"""


class Rectangle:
    """Rectangle class
    """

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            height (int, optional): _description_. Defaults to 0.
            width (int, optional): _description_. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height * self.__width

    def perimeter(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return 2 * (self.__width + self.__height)

