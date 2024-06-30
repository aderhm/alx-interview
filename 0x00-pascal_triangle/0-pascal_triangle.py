#!/usr/bin/python3
"""
Module: Representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n-1):
        prev_row = [0] + triangle[-1] + [0]
        next_row = []
        for j in range(len(triangle[-1]) + 1):
            next_row.append(prev_row[j] + prev_row[j+1])
        triangle.append(next_row)
    return triangle
