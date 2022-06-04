from typing import List


def make_connected(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    graph = [set() for _ in range(n)]

    for i, j in connections:
        graph[i].add(j)
        graph[j].add(i)

    visited = [False] * n

    def dfs(i):
        if visited[i]:
            return 0
        visited[i] = True
        for j in graph[i]:
            dfs(j)
        return 1

    return sum(dfs(i) for i in range(n)) - 1
