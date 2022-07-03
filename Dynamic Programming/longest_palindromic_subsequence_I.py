# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s: str) -> str:
    """
    Time Complexity = O(N^2)
    Space Complexity = O(N)
    """

    def find_palindrome(i, j):
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i + 1:j]

    res = ""
    n = len(s)
    for index in range(n):
        odd = find_palindrome(index, index)
        even = find_palindrome(index, index + 1)
        res = max(res, odd, even, key=len)
    return res
