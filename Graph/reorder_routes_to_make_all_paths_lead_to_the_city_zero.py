# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from typing import List
from collections import deque, defaultdict


def min_reorder_bfs(n: int, connections: List[List[int]]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(2N)
    ; N = number of nodes
    """
    graph = defaultdict(list)

    for source, destination in connections:
        graph[source].append((destination, 1))
        graph[destination].append((source, 0))

    q = deque([0])
    visited = [0] * n
    res = 0

    while q:
        city = q.popleft()
        visited[city] = 1
        for nbr, cost in graph[city]:
            if not visited[nbr]:
                res += cost
                q.append(nbr)
    return res


def min_reorder_dfs(n: int, connections: List[List[int]]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(2N)
    ; N = number of nodes
    """
    graph = defaultdict(list)

    for source, destination in connections:
        graph[source].append((destination, 1))
        graph[destination].append((source, 0))

    visited = [0] * n
    res = {"ans": 0}

    def dfs(source, res):
        visited[source] = 1
        for nbr, cost in graph[source]:
            if not visited[nbr]:
                res["ans"] += cost
                dfs(nbr, res)

    dfs(0, res)
    return res["ans"]
