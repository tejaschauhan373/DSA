# https://leetcode.com/problems/unique-paths-iii/
from typing import List


def unique_paths_III(self, grid: List[List[int]]) -> int:
    """
    Time Complexity = O(3^(m*n));
    #At every cell (except the start cell),
    we can continue the path exploration in 3 direction (after excluding previous visited cell)
    and there can be O(m*n) cells in total to be visited. In reality,
    the number of recursions required is much less due to dead-ends.
    Space Complexity = O(m*n) ; required for implicit recursive call stack
    """
    m = len(grid)
    n = len(grid[0])

    empty_count = 0
    x = None
    y = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                empty_count += 1
            elif grid[i][j] == 1:
                x, y = i, j
    self.ans = 0

    def dfs(i, j, cnt):
        if 0 <= i < m and 0 <= j < n and grid[i][j] >= 0:

            if grid[i][j] == 2:
                if cnt == -1:
                    self.ans += 1
                return
            grid[i][j] = -1
            dfs(i, j + 1, cnt - 1)
            dfs(i + 1, j, cnt - 1)
            dfs(i - 1, j, cnt - 1)
            dfs(i, j - 1, cnt - 1)
            grid[i][j] = 0

    dfs(x, y, empty_count)
    return self.ans
