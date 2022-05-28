# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List


# Graph Theory
# Array + DFS
def dfs(mat, visited, i, j, R, C):
    if visited[i][j]:
        return

    dir_x = [-1, 0, 1, 0]
    dir_y = [0, 1, 0, -1]

    visited[i][j] = True
    for k in range(4):
        cx = dir_x[k] + i
        cy = dir_y[k] + j

        if 0 <= cx < R and 0 <= cy < C:
            if mat[i][j] <= mat[cx][cy]:
                dfs(mat, visited, cx, cy, R, C)


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Time Complexity in worst case = O(N*M) ; N = number of rows, M = number of columns
    Space Complexity = O(N*M) ; N = number of rows, M = number of columns
    """
    R = len(heights)
    C = len(heights[0])

    ans = []
    pacific = [[False for _ in range(C)] for _ in range(R)]
    atlantic = [[False for _ in range(C)] for _ in range(R)]

    for i in range(C):
        dfs(heights, pacific, 0, i, R, C)
        dfs(heights, atlantic, R - 1, i, R, C)

    for j in range(R):
        dfs(heights, pacific, j, 0, R, C)
        dfs(heights, atlantic, j, C - 1, R, C)

    for i in range(R):
        for j in range(C):
            if atlantic[i][j] and pacific[i][j]:
                ans.append([i, j])

    return ans
