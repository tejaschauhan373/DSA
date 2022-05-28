# https://leetcode.com/problems/max-area-of-island/
from typing import List


# Array + DFS
def fill(grid, sr, sc, R, C):
    def dfs(r, c, count):
        if grid[r][c] == 1:
            grid[r][c] = -1
            count += 1
            if r + 1 < R: count += dfs(r + 1, c, 0)
            if r >= 1: count += dfs(r - 1, c, 0)
            if c + 1 < C: count += dfs(r, c + 1, 0)
            if c >= 1: count += dfs(r, c - 1, 0)
        return count

    return dfs(sr, sc, 0)


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Time Complexity = O(N); N = number of cells
    Space Complexity  in worst case = O(N); To store recursive call stack in DFS if all cells contain 1
    """
    R = len(grid)
    C = len(grid[0])
    max_n = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                max_n = max(fill(grid, i, j, R, C), max_n)
    return max_n
