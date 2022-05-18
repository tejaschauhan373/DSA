# https://leetcode.com/problems/word-break-ii/
from typing import List


def send_word(self, s: str, i: int, word_dict: list, ans: str, last_ans: list):
    if i >= len(s):
        last_ans.append(ans.lstrip())
        return

    temp = ""
    for j in range(i, len(s)):
        temp += s[j]
        if temp in word_dict:
            self.send_word(s, j + 1, word_dict, ans + " " + temp, last_ans)


def word_break(self, s: str, word_dict: List[str]) -> List[str]:
    """
    Time Complexity = O(N*N)
    Space Complexity = O(N) # To store call stack/ To store all words in dictionary
    """
    word_dict = {word: None for word in word_dict}
    last_ans = []
    self.send_word(s, 0, word_dict, "", last_ans)
    return last_ans
