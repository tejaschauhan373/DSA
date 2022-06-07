# https://leetcode.com/problems/palindrome-partitioning-ii/
from math import inf


def check_is_palindrome(s: str, i, j):
    while i <= j and s[i] == s[j]:
        i += 1
        j -= 1

    if i > j:
        return True
    else:
        return False


# Recursive
def min_cut(s: str) -> int:
    """
    Time Complexity = O(2^N)
    Space Complexity = O(N*N)
    ; N = len(s)
    """
    n = len(s) - 1

    def solve(s: str, i: int, j: int) -> int:

        if i == j:
            return 0

        if check_is_palindrome(s, i, j):
            return 0

        res = inf
        for k in range(i, j + 1):
            if check_is_palindrome(s, i, k):
                cost = 1 + solve(s, k + 1, j)
                res = min(res, cost)
        return res

    return solve(s, 0, n)


# Top Down
def min_cut_top_down(s: str):
    """
    Time Complexity = O(N*N)
    Space Complexity = O(N*N)
    ; N = len(s)
    """
    n = len(s) - 1
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

    def solve(s: str, i: int, j: int, dp: list) -> int:
        if i == j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]
        if check_is_palindrome(s, i, j):
            return 0

        res = inf
        for k in range(i, j + 1):
            if check_is_palindrome(s, i, k):
                cost = 1 + solve(s, k + 1, j, dp)
                res = min(res, cost)
        dp[i][j] = res
        return dp[i][j]

    return solve(s, 0, n, dp)


if __name__ == "__main__":
    string = "aab"
    print(min_cut(string))
    print(min_cut_top_down(string))
