#!/usr/bin/python3
def fizzbuzz():
    for num in range(101):
        if num % 3 and num % 5:
            print("FizzBuzz", end=" ")
        if num % 5:
            print("FizzBuzz", end=" ")
        else:
            print("Fizz", end=" ")
