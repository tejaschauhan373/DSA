# https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
# https://leetcode.com/problems/unique-binary-search-trees

# Recursive
def count_bst_brute(n: int) -> int:
    """
    Time Complexity = O(2^N)
    Space Complexity = O(N)
    """
    if n == 0 or n == 1:
        return 1

    ans = 0
    for i in range(1, n + 1):
        x = count_bst_brute(i - 1)
        y = count_bst_brute(n - i)
        ans += x * y

    return ans


# Top Down + Recursive + DP
def count_bst_dp(n: int, dp: list) -> int:
    """
    Time Complexity = O(N^2)
    Space Complexity = O(N)
    """
    if n <= 1:
        return 1

    if dp[n] != 0:
        return dp[n]

    ans = 0
    for i in range(1, n + 1):
        x = count_bst_dp(i - 1, dp)
        y = count_bst_dp(n - i, dp)
        ans += x * y

    dp[n] = ans
    return ans


# Bottom Up + Iterative + DP
def count_bst_bottom_up_dp(n: int):
    """
    Time Complexity = O(N^2)
    Space Complexity = O(N)
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]


if __name__ == "__main__":
    n = 5
    dp = [0] * (n + 1)
    print(count_bst_brute(n))
    print(count_bst_dp(n, dp))
    print(count_bst_bottom_up_dp(n))
