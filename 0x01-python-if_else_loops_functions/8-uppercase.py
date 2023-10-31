#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char) if ord(char) in
              range(65, 91) else (ord(char) - 32)), end="")
    print(res)
