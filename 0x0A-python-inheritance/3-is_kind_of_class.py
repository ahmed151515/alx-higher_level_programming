#!/usr/bin/python3
"""solve task"""


def is_kind_of_class(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        _type_: _description_
    """
    return isinstance(obj, a_class) or issubclass(obj, a_class)
