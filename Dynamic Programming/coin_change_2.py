# https://leetcode.com/problems/coin-change-2/
from functools import lru_cache
from typing import List


# Recursive
def change_recursive_brute(amount: int, coins: List[int]) -> int:
    """
    Time Complexity = O(2^N); There are redundant sub problems
    Space Complexity = O(1) + O(N)
    As no extra data structure has been used for storing values but O(N) auxiliary stack space
    (ASS) has been used for recursion stack
    ; N = len(coins)
    """
    if amount == 0:
        return 1
    elif len(coins) == 0 and amount < 0:
        return 0

    def find_denominations(amount, coins, i) -> int:
        if amount == 0:
            return 1
        elif amount < 0 or i >= len(coins):
            return 0

        return find_denominations(amount - coins[i], coins, i) + find_denominations(amount, coins, i + 1)

    return find_denominations(amount, coins, 0)


@lru_cache(maxsize=None)
def find(amount, coins, i) -> int:
    if amount == 0:
        return 1
    elif amount < 0 or i >= len(coins):
        return 0

    return find(amount - coins[i], coins, i) + find(amount, coins, i + 1)


# Recursive + LRU cache
def change_optimal_lru_cache(amount: int, coins: List[int]) -> int:
    """
    Time Complexity = O(amount * len(coins))
    Space Complexity = O(amount * len(coins)) ; For memory of LRU cache
    """
    if amount == 0:
        return 1
    elif len(coins) == 0 and amount < 0:
        return 0
    coins.sort(reverse=True)
    s = find(amount, tuple(coins), 0)
    return s


# Top Down DP
def change_optimal_top_down_dp(amount: int, coins: List[int]) -> int:
    """
    Time Complexity = O(N*W)
    Space Complexity = O(N*W)
    ; N = len(coins), W = amount
    """
    if amount == 0:
        return 1
    elif len(coins) == 0 and amount < 0:
        return 0

    dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

    def find_denom(amount, coins, i, dp) -> int:
        if amount == 0:
            return 1
        elif amount < 0 or i >= len(coins):
            return 0

        if dp[i][amount] != -1:
            return dp[i][amount]

        res = find_denom(amount - coins[i], coins, i, dp) + find_denom(amount, coins, i + 1, dp)

        dp[i][amount] = res
        return dp[i][amount]

    return find_denom(amount, coins, 0, dp)


# Bottom Up DP
def change_optimal_bottom_up(amount: int, coins: List[int]) -> int:
    """
    Time Complexity = O(N*W)
    Space Complexity = O(N*W)
    ; N = len(coins), W = amount
    """
    if amount == 0:
        return 1

    if len(coins) == 0 or amount < 0:
        return 0

    W = amount
    N = len(coins)

    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1  # because we can for 0 amount from any coins

    """
    Let's say amount = 5, coins = [1,2,5]
    W = amount = 5, N = len(coins) = 3
    
    DP Array Will be of size [N + 1][W + 1]
    
           Amount
    i,j   0 1 2 3 4 5
    
    Coins
    0     1 0 0 0 0 0
    1     1 1 1 1 1 1
    2     1 1 2 2 3 3
    3     1 1 2 2 3 4
    """
    for n in range(1, N + 1):
        for w in range(1, W + 1):
            inc = 0
            if coins[n - 1] <= w:
                inc = dp[n][w - coins[n - 1]]

            exc = dp[n - 1][w]
            dp[n][w] = inc + exc

    # print DP array
    # for row in dp:
    #     for j in row:
    #         print("%3s" % j, end="")
    #     print()
    return dp[N][W]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(change_recursive_brute(amount, coins))
    print(change_optimal_lru_cache(amount, coins))
    print(change_optimal_top_down_dp(amount, coins))
    print(change_optimal_bottom_up(amount, coins))
