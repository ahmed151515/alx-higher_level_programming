#!/usr/bin/python3
"""solve task"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """

    def print_sorted(self):
        tmp = self + []
        tmp.sort()
        print(tmp)
