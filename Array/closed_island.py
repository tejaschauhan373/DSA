# https://leetcode.com/problems/number-of-closed-islands/
from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])

    def dfs(i, j):
        grid[i][j] = 1
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < R and 0 <= y < C and grid[x][y] == 0:
                dfs(x, y)

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0 and (i == 0 or j == 0 or i == R - 1 or j == C - 1):
                dfs(i, j)

    count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                dfs(i, j)
                count += 1

    return count
