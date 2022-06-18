# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes

from typing import List


def find_smallest_set_of_vertices(n: int, edges: List[List[int]]) -> List[int]:
    """
    Time Complexity = O(n) in worst case
    Space Complexity = O(n)
    """
    count = [0] * n
    for source, destination in edges:
        count[destination] += 1  # In Degree
    res = []
    for i in range(n):
        if count[i] == 0:
            res.append(i)
    return res
