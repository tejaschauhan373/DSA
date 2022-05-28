# https://leetcode.com/problems/01-matrix
from typing import List


# Array + DP
def update_matrix(mat: List[List[int]]) -> List[List[float]]:
    """
    Time Complexity = O(N) ; N = number of cells
    Space Complexity = O(1)

    No extra space is required other than used to store the output (dist),
    and the output does not count towards the space complexity
    """
    R = len(mat)
    C = len(mat[0])

    dist = [[float("+inf") for _ in range(C)] for _ in range(R)]

    # First pass: Check for left and top
    for i in range(R):
        for j in range(C):
            if mat[i][j] == 0:
                dist[i][j] = 0
            else:
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)

                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

    # Second pass: Check for bottom and right
    i = R - 1
    while i >= 0:
        j = C - 1
        while j >= 0:
            if i < R - 1:
                dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)

            if j < C - 1:
                dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
            j -= 1
        i -= 1
    return dist
