# https://leetcode.com/problems/maximal-network-rank/
from typing import List
from collections import defaultdict


def maximal_network_rank(n: int, roads: List[List[int]]) -> int:
    """
    Time Complexity = O(N^2)
    Space Complexity = O(V+E)
    ; V = no. of vertices, E = no. of edges
    """
    connected = defaultdict(set)
    for src, dest in roads:
        connected[src].add(dest)
        connected[dest].add(src)
    max_rank = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_rank = max(max_rank, len(connected[i]) + len(connected[j]) - (i in connected[j]))
    return max_rank
