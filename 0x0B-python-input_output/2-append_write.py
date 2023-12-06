#!/usr/bin/python3
"""solve task"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """

    with open(filename, "a", encoding="UTF-8") as f:

        num = f.write("\n" + text)
