#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = [[], [], []]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res[i].append(matrix[i][j]**2)
    return res
