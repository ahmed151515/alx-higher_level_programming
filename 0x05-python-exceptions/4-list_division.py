#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    i = 0
    res = []
    while (i < list_length):
        try:

            res.append(my_list_1[i] / my_list_2[i])
            i += 1
        except (ValueError, TypeError):
            print("wrong type")
            res.append(0)
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
            i += 1
        except IndexError:
            print("out of range")
            res.append(0)
            i += 1
    return res
