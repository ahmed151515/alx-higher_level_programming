#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers:list):
    list_of_integers.sort()
    
    if len(list_of_integers) == 0:
        return None
    else:
        return list_of_integers[-1]