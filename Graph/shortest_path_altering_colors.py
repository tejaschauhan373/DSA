# https://leetcode.com/problems/shortest-path-with-alternating-colors/
from typing import List
from collections import deque


def shortest_alternating_paths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    """
    Time Complexity ~= O(kN)
    Space Complexity = O(N); N = number of nodes
    """
    graph = [[[], []] for _ in range(n)]  # O(N)
    for i, j in redEdges: graph[i][0].append(j)  # O(N)
    for i, j in blueEdges: graph[i][1].append(j)  # O(N)

    res = [[0, 0]] + [[n * 2, n * 2] for _ in range(n - 1)]  # O(N - 1)
    bfs = deque([[0, 0], [0, 1]])
    while bfs:  # O(n*2)
        i, c = bfs.popleft()
        for j in graph[i][c]:
            if res[j][c] == n * 2:
                res[j][c] = res[i][1 - c] + 1
                bfs.append([j, 1 - c])

    final_distance = []
    for i in range(len(res)):  # O(N)
        curr = min(res[i])
        if curr == n * 2:
            final_distance.append(-1)
        else:
            final_distance.append(curr)
    return final_distance
