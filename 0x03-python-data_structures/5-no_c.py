#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for i in my_string:
        if i not in "cC":
            res += i
    return res
