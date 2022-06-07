# https://leetcode.com/problems/wildcard-matching

# Recursive
def is_match_brute(s: str, p: str) -> bool:
    """
    Time Complexity = O(2^N)
    """

    def is_match_recursive(text: str, pattern: str, i: int, j: int, m: int, n: int):
        if j == n:
            return m == i

        if i < m and pattern[j] == '?':
            return is_match_recursive(text, pattern, i + 1, j + 1, m, n)
        elif pattern[j] == '*':
            assume_as_empty_string = is_match_recursive(text, pattern, i, j + 1, m, n)
            include_as_character = False
            if i < m:
                include_as_character = is_match_recursive(text, pattern, i + 1, j, m, n)
            return assume_as_empty_string or include_as_character
        elif i < m and pattern[j] == text[i]:
            return is_match_recursive(text, pattern, i + 1, j + 1, m, n)
        return False

    return is_match_recursive(s, p, 0, 0, len(s), len(p))


# Top Down DP
def is_match_top_down(s: str, p: str):
    """
    Time Complexity = O(N*M)
    Space Complexity = O(N*M)
    ; N = len(s) , M = len(p)
    """
    m = len(s)
    n = len(p)
    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    def is_match_recursive(text: str, pattern: str, i: int, j: int, m: int, n: int, dp: list):
        if j == n:
            return m == i

        if dp[i][j] != -1:
            return dp[i][j]

        res = False
        if i < m and pattern[j] == '?':
            res = is_match_recursive(text, pattern, i + 1, j + 1, m, n, dp)
        elif pattern[j] == '*':
            assume_as_empty_string = is_match_recursive(text, pattern, i, j + 1, m, n, dp)
            include_as_character = False
            if i < m:
                include_as_character = is_match_recursive(text, pattern, i + 1, j, m, n, dp)
            res = assume_as_empty_string or include_as_character
        elif i < m and pattern[j] == text[i]:
            res = is_match_recursive(text, pattern, i + 1, j + 1, m, n, dp)

        dp[i][j] = res
        return dp[i][j]

    return is_match_recursive(s, p, 0, 0, len(s), len(p), dp)


# Bottom Up DP
def is_match_bottom_up(s: str, p: str):
    """
    Time Complexity = O(N*M)
    Space Complexity = O(N*M)
    ; N = len(s) , M = len(p)
    """
    m = len(s)
    n = len(p)

    # empty pattern can only match with empty string
    if n == 0:
        return m == 0

    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

    # empty pattern can only match with empty string
    dp[0][0] = True

    # only * can match with empty string
    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]

    """
    Let's assume
    s = "acdcb", p ="a*c?b"
    m = len(s) = 5
    n = len(p) = 5
    Then DP array of size [m+1][n+1] will be
    
            Pattern 
    String  ""     a      *      c      ?     b
    
    ""    True   False  False  False  False  False
    a     False  True   True   False  False  False
    c     False  False  True   True   False  False
    d     False  False  True   False  True   False
    c     False  False  True   True   False  False
    b     False  False  True   False  True   False
    """

    # fill the table in bottom up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = False
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

    # print the dp array
    # for row in dp:
    #     for char in row:
    #         print("%6s" % char, end="")
    #     print()

    return dp[m][n]


if __name__ == "__main__":
    s = "acdcb"
    p = "a*c?b"
    print(is_match_brute(s, p))
    print(is_match_top_down(s, p))
    print(is_match_bottom_up(s, p))
