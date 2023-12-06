#!/usr/bin/python3
"""solve task"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """

    with open(filename, "w", encoding="UTF-8") as f:
        num = f.write(text)
        return num
