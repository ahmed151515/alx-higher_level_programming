#!/usr/bin/python3
"""solve task"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".

    Raises:
        TypeError: _description_
        TypeError: _description_
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
