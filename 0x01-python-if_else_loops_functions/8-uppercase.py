#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        if ord(char) in range(97, 123):
            res += "{:c}".format(ord(char) - 32)
        else:
            res+ "{:c}".format(ord(char))
