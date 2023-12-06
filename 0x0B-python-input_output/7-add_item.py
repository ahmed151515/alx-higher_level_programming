#!/usr/bin/python3
"""solve task"""


import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    data = load_from_json_file("add_item.json")
except Exception:
    data = []
for i in list(argv[1:]):
    data.append(i)

save_to_json_file(data, "add_item.json")
