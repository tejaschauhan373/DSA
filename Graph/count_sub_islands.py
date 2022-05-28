# https://leetcode.com/problems/count-sub-islands/


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


def count_sub_islands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    """
    Time Complexity = O(N); N = number of cells
    Space Complexity = O(1)
    """
    R = len(grid1)
    C = len(grid1[0])

    for i in range(R):
        for j in range(C):
            if grid2[i][j] == 1 and grid1[i][j] == 0:
                fill(grid2, i, j, R, C)
    res = 0
    for i in range(R):
        for j in range(C):
            if grid2[i][j] == 1:
                res += 1
                fill(grid2, i, j, R, C)
    return res
