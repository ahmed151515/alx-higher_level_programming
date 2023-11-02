#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{} argument:".format(len(argv)))
    for i in range(1, len(argv)):
        print("{} {}".format(i, argv[i]))
