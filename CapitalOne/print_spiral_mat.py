from typing import List

#!/usr/bin/env python3
"""
print_spiral_mat.py

Simple utility to produce the elements of a 2D matrix in spiral order
and print them.
"""


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Return the elements of matrix in spiral order."""
    if not matrix or not matrix[0]:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    out: List[int] = []

    while top <= bottom and left <= right:
        # left -> right on top row
        for j in range(left, right + 1):
            out.append(matrix[top][j])
        top += 1

        # top -> bottom on right column
        for i in range(top, bottom + 1):
            out.append(matrix[i][right])
        right -= 1

        # right -> left on bottom row
        if top <= bottom:
            for j in range(right, left - 1, -1):
                out.append(matrix[bottom][j])
            bottom -= 1

        # bottom -> top on left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                out.append(matrix[i][left])
            left += 1

    return out

def print_spiral(matrix: List[List[int]]) -> None:
    """Print the spiral order of the matrix on one line."""
    print(" ".join(map(str, spiral_order(matrix))))

if __name__ == "__main__":
    # Example usages
    mats = [
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9,10,11,12]],

        [[1]],

        [],            # empty matrix
        [[]],          # matrix with empty row
    ]

    for m in mats:
        print_spiral(m)