#!/usr/bin/python3
"""solve task"""


import json
from sys import argv
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

with open("add_item.json", "r+") as f:

    data = load_from_json_file(f)
    for i in argv:
        data.append(i)

    save_to_json_file(data, "add_item.json")
