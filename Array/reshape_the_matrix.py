# https://leetcode.com/problems/reshape-the-matrix/
from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    """
    Time Complexity = O(m*n) ; m = no. of rows, n = no. of columns
    Space Complexity = O(1)
    """
    m, n = len(mat), len(mat[0])
    if r * c != m * n:
        return mat
    ans = [[0] * c for _ in range(r)]
    for i in range(m * n):
        ans[i // c][i % c] = mat[i // n][i % n]
    return ans
