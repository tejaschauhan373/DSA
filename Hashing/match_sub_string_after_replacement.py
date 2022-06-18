# https://leetcode.com/problems/match-substring-after-replacement/
from collections import defaultdict
from typing import List


def match_replacement(s: str, sub: str, mappings: List[List[str]]) -> bool:
    """
    Time Complexity = O(N*k)
    Space Complexity = O(k)
    ; N = len(s), k = len(sub)
    """
    hash_map = defaultdict(set)

    for char, substitute in mappings:
        hash_map[char].add(substitute)

    n = len(sub)

    for i in range(len(s) - len(sub) + 1):
        got = True
        for s_val, sub_val in zip(s[i:i + n], sub):
            if s_val == sub_val or (s_val in hash_map[sub_val]):
                continue
            else:
                got = False
                break
        if got:
            return True
    return False
