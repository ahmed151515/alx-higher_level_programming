#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digt = number % 10
if last_digt == 0:
    print(f"Last digit of {number} is {last_digt} and is 0")
elif number % 10 < 6:
    print(f"Last digit of {number} is {last_digt} and is less than 6 and not 0")
elif number % 10 > 5:
    print(f"Last digit of {number} is {last_digt} and is greater than 5")
