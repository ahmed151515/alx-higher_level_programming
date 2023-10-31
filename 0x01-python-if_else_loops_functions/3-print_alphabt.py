#!/usr/bin/python3
for char in range(97, 123):
    if char in [101, 113]:
        continue
    print("{:c}".format(char),end="")
