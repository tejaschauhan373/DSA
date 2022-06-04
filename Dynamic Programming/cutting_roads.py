from math import inf


# Recursive
def max_profit_top_down_brute(prices: list, n: int):
    """
    Time Complexity = O(N^N)
    Space Complexity = O(N^N) ; To store recursive call stack
    """
    if n <= 0:
        return 0

    ans = -inf

    for i in range(n):
        cut = i + 1
        current_ans = prices[i] + max_profit_top_down_brute(prices, n - cut)
        ans = max(ans, current_ans)

    return ans


# Recursive + Top Down + Memoization
def max_profit_top_down_optimal(prices: list, n: int, dp: dict):
    """
    Time Complexity = O(N*N) = O(N^2)
    Space Complexity = O(N+1)
    """
    if n in dp:
        return dp[n]
    if n <= 0:
        return 0

    ans = -inf

    for i in range(n):
        cut = i + 1
        current_ans = prices[i] + max_profit_top_down_optimal(prices, n - cut, dp)
        ans = max(ans, current_ans)
    dp[n] = ans
    return dp[n]


# Iterative + Bottom Up
def max_profit_bottom_up(prices: list, n: int):
    """
    Time Complexity = O(N^2)
    Space Complexity = O(N+1)
    """
    dp = [0] * (n + 1)
    dp[0] = 0

    for length in range(1, n + 1):
        ans = -inf
        for i in range(length):
            cut = i + 1
            current_ans = prices[i] + dp[length - cut]
            ans = max(current_ans, ans)
        dp[length] = ans
        # Computed the ans for dp[length]

    return dp[n]


if __name__ == "__main__":
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    n = len(prices)
    print(max_profit_top_down_brute(prices, n))
    print(max_profit_top_down_optimal(prices, n, {}))
    print(max_profit_bottom_up(prices, n))
