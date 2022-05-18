# https://leetcode.com/problems/word-break

# Hash Table + DP
from typing import List


def send_word(self, s: str, i: int, word_dict: list, dp: dict):
    if i >= len(s):
        return True

    temp = ""
    for j in range(i, len(s)):
        temp += s[j]
        if temp in word_dict:
            if j + 1 in dp:
                res = dp[j + 1]
            else:
                res = self.send_word(s, j + 1, word_dict, dp)
                dp[j + 1] = res
            if res:
                return True
    return False


def word_break(self, s: str, word_dict: List[str]) -> bool:
    """
    Time Complexity in worst case = O(N*N) ; N = length of string s
    Space Complexity in worst case = O(N) ; N = length of string s
    """
    word_dict = {word: None for word in word_dict}
    return self.send_word(s, 0, word_dict, {})
