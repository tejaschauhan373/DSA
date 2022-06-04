# Recursive
def lcs_brute(s1: str, s2: str, i: int, j: int) -> int:
    # base case
    if i == len(s1) or j == len(s2): return 0

    # recursive case
    if s1[i] == s2[j]:
        return 1 + lcs_brute(s1, s2, i + 1, j + 1)

    op1 = lcs_brute(s1, s2, i + 1, j)
    op2 = lcs_brute(s1, s2, i, j + 1)
    return max(op1, op2)


# Top Down + Memoization
def lcs_dp(s1: str, s2: str, i: int, j: int, dp: list) -> int:
    # base case
    if i == len(s1) or j == len(s2): return 0

    # check if state is already computed
    if dp[i][j] != -1:
        return dp[i][j]

    # recursive case
    if s1[i] == s2[j]:
        res = 1 + lcs_dp(s1, s2, i + 1, j + 1, dp)
        dp[i][j] = res
    else:
        op1 = lcs_dp(s1, s2, i + 1, j, dp)
        op2 = lcs_dp(s1, s2, i, j + 1, dp)
        res = max(op1, op2)

    dp[i][j] = res
    return dp[i][j]


# Bottom Up
def lcs_bottom_up(s1: str, s2: str) -> int:
    l1 = len(s1)
    l2 = len(s2)

    # DP Array
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    # 1, 1, ..., n1, n2
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                op1 = dp[i - 1][j]
                op2 = dp[i][j - 1]
                dp[i][j] = max(op1, op2)

    # Print the matrix
    # for i in range(l1 + 1):
    #     for j in range(l2 + 1):
    #         print(dp[i][j], end=" ")
    #     print()

    # get the common characters in correct order
    result = []
    i = l1
    j = l2
    while i != 0 and j != 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
    for char in result:
        print(char, end="")
    print()

    return dp[l1][l2]


if __name__ == "__main__":
    s1 = "ABCD"
    s2 = "ABEDG"
    l1 = len(s1)
    l2 = len(s2)
    dp = [[-1 for _ in range(l2)] for _ in range(l1)]
    print(lcs_brute(s1, s2, 0, 0))
    print(lcs_dp(s1, s2, 0, 0, dp))
    print(lcs_bottom_up(s1, s2))
