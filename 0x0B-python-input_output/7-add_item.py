#!/usr/bin/python3
"""solve task"""


import json
from sys import argv
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


data = load_from_json_file("add_item.json")
for i in list(argv[1:]):
    data.append(i)

save_to_json_file(data, "add_item.json")
