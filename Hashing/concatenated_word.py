# https://leetcode.com/problems/concatenated-words
from typing import List


# Hash table + DP

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


def word_break(self, s: str, word_dict: dict) -> bool:
    return self.send_word(s, 0, word_dict, {})


def find_all_concatenated_words_in_a_dict(self, words: List[str]) -> List[str]:
    """
    Time Complexity in worst case = O(N*N) ; N = number of words
    Space Complexity in worst case = O(N) ; N = number of words
    """
    words.sort(key=len, reverse=True)
    word_dict = {word: None for word in words}
    ans = []
    for i, word in enumerate(words):
        del word_dict[word]
        if len(word) == 0:
            continue
        res = self.wordBreak(word, word_dict)
        if res:
            ans.append(word)
    return ans
