#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = []
    for i in my_list:
        if i == search:
            res.append(replace)
        else:
            res.append(i)
    return res
