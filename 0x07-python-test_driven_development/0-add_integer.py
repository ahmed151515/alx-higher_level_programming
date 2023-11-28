#!/usr/bin/python3
"""solve task"""


def add_integer(a, b=98):
    """add to number

    Args:
        a (int): num 1
        b (int, optional): num 2. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: a + b
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
