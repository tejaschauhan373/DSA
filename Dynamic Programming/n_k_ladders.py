# Recursive (Brute Force)
def count_ways_brute(n: int, k: int) -> int:
    """
    Time Complexity = O(k^N)
    """
    if n == 0:
        return 1
    if n < 0:
        return 0

    # recursive case
    ans = 0
    for jump in range(1, k + 1):
        ans += count_ways_brute(n - jump, k)

    return ans


# Top Down Code
def count_ways_dp(n: int, k: int, dp: list):
    """
    Time Complexity = O(N*k)
    """
    if n == 0:
        return 1

    if n < 0:
        return 0

    # Check if state is already computed
    if dp[n] != 0:
        return dp[n]

    # Recursive case
    ans = 0
    for jump in range(1, k + 1):
        ans += count_ways_dp(n - jump, k, dp)

    dp[n] = ans
    return dp[n]


# Bottom Up Approach (Iterative)
def count_ways_bottom_up(n: int, k: int):
    """
    Time Complexity = O(N*k)
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for jump in range(1, k + 1):
            if i - jump >= 0:
                dp[i] += dp[i - jump]

    return dp[n]


# Bottom Up - Optimised
def count_ways_bottom_up_optimised(n: int, k: int):
    """
    Time Complexity = O(N+k)
    """
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, k + 1):
        dp[i] = 2 * dp[i - 1]

    for i in range(k + 1, n + 1):
        dp[i] = 2 * dp[i - 1] - dp[i - k - 1]

    return dp[n]


if __name__ == "__main__":
    n = 6
    k = 3
    dp = [0] * (n + 6)
    print(count_ways_brute(n, k))
    print(count_ways_dp(n, k, dp))
    print(count_ways_bottom_up(n, k))
    print(count_ways_bottom_up_optimised(n, k))
