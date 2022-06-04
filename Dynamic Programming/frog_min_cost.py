# Bottom Up + Iterative
def find_min_cost(stones: list):
    """
    Time Complexity = O(N)
    """
    n = len(stones)
    dp = [0] * n
    dp[1] = abs(stones[1] - stones[0])

    for i in range(2, n):
        op1 = abs(stones[i] - stones[i - 1]) + dp[i - 1]
        op2 = abs(stones[i] - stones[i - 2]) + dp[i - 2]
        dp[i] = min(op1, op2)

    return dp[n - 1]


if __name__ == "__main__":
    arr = [30, 10, 60, 10, 60, 50]
    print(find_min_cost(arr))
