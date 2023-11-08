#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    for key in sorted_dic:
        print(f"{key}: {a_dictionary.get(key)}")
