#!/usr/bin/python3
"""solve task"""


def matrix_divided(matrix, div):
    """divid all elements of a matrix.

    Args:
        matrix (2-d list): 2-Dimntios list
        div (number): num

    Raises:
        TypeError: _description_
        ZeroDivisionError: _description_
        TypeError: _description_
        TypeError: _description_
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    length = len(matrix[0])
    lsit_num = 0
    result = []
    for nums in matrix:
        if len(nums) != length:
            raise TypeError("Each row of the matrix \
must have the same size")
        result.append([])
        for num in nums:
            if type(num) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix \
(list of lists) of integers/floats")
            result[lsit_num].append(round(float(num / div), 2))
        lsit_num += 1
    return result


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
