# https://leetcode.com/problems/max-area-of-island
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    max_n = 0

    def dfs(r, c, count):
        if grid[r][c] == 1:
            grid[r][c] = -1
            count += 1
            if r + 1 < R: count += dfs(r + 1, c, 0)
            if r >= 1: count += dfs(r - 1, c, 0)
            if c + 1 < C: count += dfs(r, c + 1, 0)
            if c >= 1: count += dfs(r, c - 1, 0)
        return count

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                max_n = max(dfs(i, j, 0), max_n)
    return max_n
