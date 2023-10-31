#!/usr/bin/python3
for num in range(99):
    print("{:s}{:d}".format("0" if num < 10 else "", num), end=", ")
else:
    print(99)
