#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    tmp = []  # Recurring
    for i in my_list:
        if i in tmp:
            continue
        tmp.append(i)
        sum += i
    return sum
