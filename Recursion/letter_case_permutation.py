# https://leetcode.com/problems/letter-case-permutation/
from typing import List


def letterCasePermutation(s: str) -> List[str]:
    ans = []

    def permute(s: str, i: int, n: int):
        nonlocal ans
        if i == n:  # base case
            ans.append(s)
            return

        if s[i].isalpha():  # recursive case
            if s[i].islower():
                permute(s, i + 1, n)
                permute(s[:i] + s[i].upper() + s[i + 1:], i + 1, n)
            else:
                permute(s, i + 1, n)
                permute(s[:i] + s[i].lower() + s[i + 1:], i + 1, n)
        else:
            permute(s, i + 1, n)

    permute(s, 0, len(s))
    return ans
