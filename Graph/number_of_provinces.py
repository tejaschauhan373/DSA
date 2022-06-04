# https://leetcode.com/problems/number-of-provinces/
from typing import List


def dfs(i, isc, visited):
    for j in range(len(visited)):
        if isc[i][j] == 1 and not visited[j]:
            visited[j] = 1
            dfs(j, isc, visited)


def find_circle_num(is_connected: List[List[int]]) -> int:
    visited = [False] * len(is_connected)
    parts = 0
    for i in range(len(is_connected)):
        if not visited[i]:
            parts += 1
            dfs(i, is_connected, visited)
    return parts


print(find_circle_num([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
