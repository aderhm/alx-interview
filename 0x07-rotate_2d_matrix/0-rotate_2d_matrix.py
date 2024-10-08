#!/usr/bin/python3
""" Module: Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate a given n*n 2D matrix  90 degrees clockwise
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
