# https://leetcode.com/problems/min-cost-climbing-stairs

"""
Recursive Case:
mincost[i] = cost[i] + min(mincost[i - 1] , mincost[i -2])

Base Case:
mincost[0] = cost[0]
mincost[1] = cost[1]
"""


# Recursive
def min_cost_top_down_brute(cost: list):
    """
    Time Complexity = O(2^N)
    """
    n = len(cost)

    def find_min_cost(i):
        if i < 0:
            return 0
        if i == 0 or i == 1:
            return cost[i]

        return cost[i] + min(find_min_cost(i - 1), find_min_cost(i - 2))

    return min(find_min_cost(n - 1), find_min_cost(n - 2))


# Top Down + Memoization
def min_cost_top_down_memoization(cost: list):
    """
    Time Complexity = O(n)
    Space Complexity = O(n)
    """
    n = len(cost)
    dp = [0] * n

    def find_min_cost(i):
        # base case
        if i < 0:
            return 0
        if i == 0 and i == 1:
            return cost[i]

        if dp[i] != 0:
            return dp[i]

        # recursive case
        dp[i] = min(find_min_cost(i - 1), find_min_cost(i - 2))
        return dp[i]

    return min(find_min_cost(n - 1), find_min_cost(n - 2))


# Bottom Up + Iterative
def min_cost_bottom_up(cost: list):  # Getting rid of recursive call stack
    """
    Time Complexity = O(n)
    Space Complexity = O(n)
    """
    n = len(cost)
    dp = [0] * n
    # base case
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])


# Fine tuning reduce O(N) space to O(1)
def min_cost_bottom_up_optimized(cost: list):
    """
    Time Complexity = O(n)
    Space Complexity = O(1)
    """
    n = len(cost)
    # base case
    first = cost[0]
    second = cost[1]
    if n <= 2:
        return min(first, second)

    for i in range(2, n):
        curr = cost[i] + min(first, second)
        first = second
        second = curr

    return min(first, second)
