# https://leetcode.com/problems/unique-paths-ii
from typing import List


def uniqueP_paths_with_obstacles_brute(obstacleGrid: List[List[int]]) -> int:
    """
    Time Complexity = O(2^(m+n))
    Space Complexity = O(m+n); required to maintain dp
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    if obstacleGrid[m - 1][n - 1] == 1:
        return 0

    def dfs(i, j):
        if i == m - 1 and j == n - 1:
            return 1

        if i >= m or j >= n:
            return 0

        if obstacleGrid[i][j] == 1:
            return 0

        return dfs(i + 1, j) + dfs(i, j + 1)

    return dfs(0, 0)


def unique_paths_with_obstacles_dp(obstacleGrid: List[List[int]]) -> int:
    """
    Time Complexity = O(m*n)
    Space Complexity = O(m*n); required to maintain dp
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[-1] * n for _ in range(m)]

    if obstacleGrid[m - 1][n - 1] == 1:
        return 0

    def dfs(i, j, dp):
        if i == m - 1 and j == n - 1:
            return 1

        if i >= m or j >= n:
            return 0

        if obstacleGrid[i][j] == 1:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = dfs(i + 1, j, dp) + dfs(i, j + 1, dp)
        return dp[i][j]

    return dfs(0, 0, dp)
