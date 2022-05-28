# https://leetcode.com/problems/find-eventual-safe-states/
import collections
from typing import List


def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    """
    Time Complexity = O(N+E); N = number of nodes, E = total number of edges
    Space Complexity = O(N)
    """
    N = len(graph)
    safe = [False] * N

    graph = [set(neighbor) for neighbor in graph]
    rgraph = [set() for _ in range(N)]
    q = collections.deque()

    for i, js in enumerate(graph):
        if not js:
            q.append(i)
        for j in js:
            rgraph[j].add(i)

    while q:
        curr = q.popleft()
        safe[curr] = True
        for i in rgraph[curr]:
            graph[i].remove(curr)
            if len(graph[i]) == 0:
                q.append(i)

    return [i for i, is_safe in enumerate(safe) if is_safe]


print(eventual_safe_nodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
