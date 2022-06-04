# Recursive Brute Force
def count_sub_sequence_brute(s1: str, s2: str, i: int, j: int):
    # base case
    if (i == -1 and j == - 1) or j == -1:
        return 1

    if i == -1:
        return 0

    # recursive case
    if s1[i] == s2[j]:
        first = count_sub_sequence_brute(s1, s2, i - 1, j - 1)
        second = count_sub_sequence_brute(s1, s2, i - 1, j)
        return first + second
    else:
        return count_sub_sequence_brute(s1, s2, i - 1, j)


# Top Down DP
def count_sub_sequence_top_down(s1: str, s2: str, i: int, j: int, dp: list):
    # base case
    if (i == -1 and j == -1) or j == -1:
        return 1

    if i == -1:
        return 0

    # Check if it is already computed
    if dp[i][j] != -1:
        return dp[i][j]

    # recursive case
    if s1[i] == s2[j]:
        first = count_sub_sequence_top_down(s1, s2, i - 1, j - 1, dp)
        second = count_sub_sequence_top_down(s1, s2, i - 1, j, dp)
        res = first + second
    else:
        res = count_sub_sequence_top_down(s1, s2, i - 1, j, dp)

    dp[i][j] = res
    return dp[i][j]


# Bottom Up
def count_sub_sequence_bottom_up(s1: str, s2: str):
    m = len(s1)
    n = len(s2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table in bottom up manner
    # First col as 1

    for i in range(m + 1):
        dp[i][0] = 1

    # 1,1, .., m,n
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]


if __name__ == "__main__":
    a = "ACBCECDGCC"
    b = "ABC"
    print(count_sub_sequence_brute(a, b, len(a) - 1, len(b) - 1))
    dp = [[-1 for _ in range(len(b))] for _ in range(len(a))]
    print(count_sub_sequence_top_down(a, b, len(a) - 1, len(b) - 1, dp))
    print(count_sub_sequence_bottom_up(a, b))
