#!/usr/bin/python3
"""solve task"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): is the size length of the square

    Raises:
        TypeError: _description_
        ValueError: _description_
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
