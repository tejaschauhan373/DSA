# https://leetcode.com/problems/coin-change
from math import inf


# Top Down Approach + Recursive + DP
def min_number_of_coins_for_change_top_dwn(m: int, denoms: list, dp: dict) -> int:
    if m in dp:
        return dp[m]
    if m < 0:
        return -1
    if m == 0:
        return 0

    min_change = inf
    for coin in denoms:
        count = min_number_of_coins_for_change_top_dwn(m - coin, denoms, dp)
        if count != -1:
            min_change = min(min_change, 1 + count)

    if min_change == inf:
        dp[m] = -1
    else:
        dp[m] = min_change

    return dp[m]


# Bottom Up Approach + DP
def min_number_of_coins_for_change_btm_up(m: int, denoms: list) -> int:
    """
    Time Complexity in worst case= O(m*len(denoms))
    Space Complexity = O(m + 1); To store possible minimum denomination in dp array
    """
    dp = [0] * (m + 1)
    dp[0] = 0

    for i in range(1, m + 1):
        dp[i] = float("+inf")
        for c in denoms:
            if i - c >= 0 and dp[i - c] != float("+inf"):
                dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[m] == float("+inf"):
        return -1
    else:
        return dp[m]


if __name__ == "__main__":
    denoms = [1, 5, 7, 10]
    m = 18
    print(min_number_of_coins_for_change_btm_up(m, denoms))
    print(min_number_of_coins_for_change_top_dwn(m, denoms, {}))
