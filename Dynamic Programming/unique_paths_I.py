# https://leetcode.com/problems/unique-paths/


def unique_paths_brute(m: int, n: int) -> int:
    """
    Time Complexity = O(2^(m+n))
    Space Complexity = O(m+n); required to maintain dp
    """
    def dfs(i, j):
        if i == m - 1 and j == n - 1:
            return 1

        if i >= m or j >= n:
            return 0

        return dfs(i + 1, j) + dfs(i, j + 1)

    return dfs(0, 0)


def unique_paths_dp(m: int, n: int) -> int:
    """
    Time Complexity = O(m*n)
    Space Complexity = O(m*n); required to maintain dp
    """
    dp = [[-1] * n for _ in range(m)]

    def dfs(i, j):
        nonlocal dp
        if i == m - 1 and j == n - 1:
            return 1

        if i >= m or j >= n:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = dfs(i + 1, j) + dfs(i, j + 1)

        return dp[i][j]

    return dfs(0, 0)
