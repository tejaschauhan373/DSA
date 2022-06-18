# https://leetcode.com/problems/open-the-lock
from collections import deque
from typing import List


def open_lock(dead_ends: List[str], target: str) -> int:
    """
    Time Complexity = O(N)
    Space  Complexity = O(N)
    ; N = number of strings in dead ends
    """
    depth = -1
    visited = set(dead_ends)
    q = deque(['0000'])

    while q:
        size = len(q)
        depth += 1
        for _ in range(size):
            node = q.popleft()
            if node == target: return depth
            if node in visited: continue
            visited.add(node)
            for i, ch in enumerate(node):
                num = int(ch)
                q.append(f"{node[:i]}{(num - 1) % 10}{node[i + 1:]}")
                q.append(f"{node[:i]}{(num + 1) % 10}{node[i + 1:]}")
    return -1
