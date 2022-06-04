# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import defaultdict
from typing import List


# String + Hashing + Sliding Window
def find_anagrams(s: str, p: str) -> List[int]:
    p_char_count = defaultdict(int)
    res = []
    length_of_p = len(p)
    length_of_s = len(s)

    if length_of_p > length_of_s:
        return []

    for ch in p:
        p_char_count[ch] += 1

    for i in range(length_of_p - 1):
        if s[i] in p_char_count:
            p_char_count[s[i]] -= 1

    for i in range(-1, length_of_s - length_of_p + 1):
        if i > -1 and s[i] in p_char_count:
            p_char_count[s[i]] += 1

        next_char_index = i + length_of_p
        if i + length_of_p < length_of_s and s[next_char_index] in p_char_count:
            p_char_count[s[next_char_index]] -= 1

        # check whether we encountered an anagram
        if all(v == 0 for v in p_char_count.values()):
            res.append(i + 1)

    return res
