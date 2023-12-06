#!/usr/bin/python3
"""solve task"""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, encoding="UTF-8") as file:
        print(file.read())
