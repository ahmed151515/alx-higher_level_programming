#!/usr/bin/python3

import json
from sys import argv
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

# Load existing data from the file or create an empty list
    data = load_from_json_file("add_item.json")
    data = []

# Add command line arguments to the list
data.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(data, "add_item.json")

