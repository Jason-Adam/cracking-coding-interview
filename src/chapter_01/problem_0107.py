# Rotate Matrix:
# Given an image represented by an N x N matrix, where each
# pixel in the image is represented by an integer, write a method
# to rotate the image by 90 degrees. Can you do this in place?

from typing import List


def rotate_matrix(matrix: List[List[int]]) -> bool:
    """O(n^2) time | O(1) space
    Updates matrix in place
    """
    # Validate that matrix is N x N
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    for layer in range(0, int(n / 2)):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top

    return True
