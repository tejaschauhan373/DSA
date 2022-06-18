# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516973/JavaPython-3-Sliding-Window-O(n)-O(1)-code-w-explanation-and-analysis.


def number_of_sub_strings(s: str) -> int:
    """
    Time Complexity = O(N) ; N = len(s)
    Space Complexity = O(1)
    """
    cnt = {char: 0 for char in 'abc'}
    res = 0
    low = -1
    for high, char in enumerate(s):
        cnt[char] += 1
        while all(cnt.values()):
            res += len(s) - high
            low += 1
            cnt[s[low]] -= 1
    return res
