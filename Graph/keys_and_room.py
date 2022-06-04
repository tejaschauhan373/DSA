# https://leetcode.com/problems/keys-and-rooms/
from typing import List


# DFS
def can_visit_all_rooms_iterative(rooms: List[List[int]]) -> bool:
    visited = [False] * len(rooms)

    visited[0] = True

    keys = rooms[0]

    while keys:
        curr = keys.pop()
        if not visited[curr]:
            visited[curr] = True
            keys += rooms[curr]
    return all(visited)
