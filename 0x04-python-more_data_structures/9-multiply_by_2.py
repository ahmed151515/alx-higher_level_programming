#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_n = {}
    for key, value in a_dictionary.items():
        dic_n[key] = value*2
    return dic_n
