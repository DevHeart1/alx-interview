#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a two-dimensional matrix 90 degrees clockwise.

    Args:
        matrix (list[list]): A matrix to rotate.
    """
    n = len(matrix)
    for i in range(n // 2):
        y = n - i - 1
        for j in range(i, y):
            x = n - 1 - j
            # Current number
            tmp = matrix[i][j]
            # Change top for left
            matrix[i][j] = matrix[x][i]
            # Change left for bottom
            matrix[x][i] = matrix[y][x]
            # Change bottom for right
            matrix[y][x] = matrix[j][y]
            # Change right for top
            matrix[j][y] = tmp
