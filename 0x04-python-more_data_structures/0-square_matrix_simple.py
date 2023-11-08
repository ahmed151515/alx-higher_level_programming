#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return []
    res = [matrix[0].copy(), matrix[1].copy(), matrix[2].copy()]
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = res[i][j]**2
    return res
