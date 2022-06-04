# Recursive
def knapsack(weights: list, prices: list, N: int, W: int) -> int:
    # base case
    if N == 0 or W == 0:
        return 0

    # recursive case
    inc = 0
    if weights[N - 1] <= W:
        inc = prices[N - 1] + knapsack(weights, prices, N - 1, W - weights[N - 1])

    exc = knapsack(weights, prices, N - 1, W)

    return max(inc, exc)


# Top Down
def knapsack_top_down(weights: list, prices: list, N: int, W: int, dp: list) -> int:
    # base case
    if N == 0 or W == 0:
        return 0

    # Check if it is already computed
    if dp[N][W] != -1:
        return dp[N][W]

    # recursive case
    inc = 0
    if weights[N - 1] <= W:
        inc = prices[N - 1] + knapsack_top_down(weights, prices, N - 1, W - weights[N - 1], dp)

    exc = knapsack_top_down(weights, prices, N - 1, W, dp)

    dp[N][W] = max(inc, exc)
    return dp[N][W]


# Bottom Up
def knapsack_bottom_up(weights: list, prices: list, N: int, W: int) -> int:
    """
    Time Complexity = O(N*W)
    Space Complexity = O(N*W)
    """

    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            inc = 0
            if weights[n - 1] <= w:
                inc = prices[n - 1] + dp[n - 1][w - weights[n - 1]]

            exc = dp[n - 1][w]

            dp[n][w] = max(inc, exc)

    # print top down DP table
    # for row in dp:
    #     for ele in row:
    #         print("%3s" % ele, end="")
    #     print()

    return dp[N][W]


if __name__ == "__main__":
    wts = [2, 7, 3, 4]
    amounts = [5, 20, 20, 10]
    n = 4
    w = 11
    print(knapsack(wts, amounts, n, w))
    dp = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]
    print(knapsack_top_down(wts, amounts, n, w, dp))
    # print bottom up dp table
    # for row in dp:
    #     for ele in row:
    #         print("%3s" % ele, end="")
    #     print()
    print(knapsack_bottom_up(wts, amounts, n, w))
