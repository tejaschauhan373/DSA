# https://leetcode.com/problems/number-of-enclaves/
from typing import List


# Array + DFS
def fill(grid, sr, sc, R, C):
    def dfs(r, c):
        if grid[r][c] == 1:
            grid[r][c] = 0
            if r + 1 < R: dfs(r + 1, c)
            if r >= 1: dfs(r - 1, c)
            if c + 1 < C: dfs(r, c + 1)
            if c >= 1: dfs(r, c - 1)

    dfs(sr, sc)


def num_enclaves(grid: List[List[int]]) -> int:
    """
    Time Complexity = O(N); N = number of cells
    Space Complexity  in worst case = O(N); To store recursive call stack in DFS if all cells contain 1
    """
    R = len(grid)
    C = len(grid[0])
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                if grid[i][j] == 1:
                    fill(grid, i, j, R, C)
    return sum(sum(row) for row in grid)
