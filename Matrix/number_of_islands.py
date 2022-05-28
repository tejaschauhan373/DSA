# https://leetcode.com/problems/number-of-islands/
from typing import List


def fill(grid, sr, sc, R, C):
    def dfs(r, c):
        if grid[r][c] == "1":
            grid[r][c] = "*"
            if r + 1 < R: dfs(r + 1, c)
            if r >= 1: dfs(r - 1, c)
            if c + 1 < C: dfs(r, c + 1)
            if c >= 1: dfs(r, c - 1)

    dfs(sr, sc)


def num_is_lands(grid: List[List[str]]) -> int:
    """
    Time Complexity = O(N) ; N = Number of cells
    Space Complexity in worst case = O(N) ; To store DFS recursive call stack, in case of having '1' in all cell
    """
    R = len(grid)
    C = len(grid[0])
    res = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "1":
                res += 1
                fill(grid, i, j, R, C)
    return res
