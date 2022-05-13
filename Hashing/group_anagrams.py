# https://leetcode.com/problems/group-anagrams
import collections
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    hmap = collections.defaultdict(list)
    for st in strs:  # TC = O(N); N = No of Words
        array = [0] * 26  # TC = O(1)
        for l in st:  # TC = O(1)
            array[ord(l) - ord('a')] += 1
        hmap[tuple(array)].append(st)  # O(1)
    return list(hmap.values())


def group_anagrams_second(strs: List[str]) -> List[List[str]]:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return list(d.values())
