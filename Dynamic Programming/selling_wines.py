# https://www.udemy.com/course/cpp-data-structures-algorithms-levelup-prateek-narang/learn/lecture/25798292#questions
# Top Down + Brute
def wines_brute(prices: list, L: int, R: int, y: int) -> int:
    # base case
    if L > R:
        return 0

    if dp[L][R] != 0:
        return dp[L][R]

    # recursive case
    pick_left = y * prices[L] + wines_brute(prices, L + 1, R, y + 1)
    pick_right = y * prices[R] + wines_brute(prices, L, R - 1, y + 1)

    return max(pick_left, pick_right)


# Top Down DP
def wines_top_down(dp: list, prices: list, L: int, R: int, y: int):
    # base case
    if L > R:
        return 0

    if dp[L][R] != 0:
        return dp[L][R]

    # recursive case
    pick_left = y * prices[L] + wines_top_down(dp, prices, L + 1, R, y + 1)
    pick_right = y * prices[R] + wines_top_down(dp, prices, L, R - 1, y + 1)

    dp[L][R] = max(pick_left, pick_right)
    return dp[L][R]


# Bottom Up DP
def wines_bottom_up(prices: list, n: int):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    i = n - 1
    while i >= 0:
        j = 0

        # bottom row to top row
        while j < n:
            if i == j:
                dp[i][j] = n * prices[i]
            elif i < j:
                # dp(i...j)
                y = n - (j - i)
                pick_left = prices[i] * y + dp[i + 1][j]
                pick_right = prices[j] * y + dp[i][j - 1]
                dp[i][j] = max(pick_left, pick_right)
            j += 1
        i -= 1

    # print bottom up matrix
    # for i in range(n):
    #     for j in range(n):
    #         print(dp[i][j], end=" ")
    #     print()

    return dp[0][n - 1]


if __name__ == "__main__":
    prices = [2, 3, 5, 1, 4]
    dp = [[0 for _ in range(len(prices))] for _ in range(len(prices))]
    print(wines_brute(prices, 0, len(prices) - 1, 1))
    print(wines_top_down(dp, prices, 0, len(prices) - 1, 1))
    print(wines_bottom_up(prices, len(prices)))
