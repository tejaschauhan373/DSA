# https://leetcode.com/problems/jump-game-iii/
from typing import List
from collections import deque


# DFS + Recursive
def canReach(arr: List[int], start: int) -> bool:
    """
    Time Complexity = O(N) ; N = len(arr)
    Space Complexity = O(N) in worst case, N = len(arr) ; To store recursive call in stack
    """
    n = len(arr)
    visited = [False] * n
    res = {"ans": False}

    def dfs(source):
        nonlocal visited, res
        visited[source] = True

        if arr[source] == 0:
            res["ans"] = True
            return

        forward = source + arr[source]
        if forward < len(arr) and not visited[forward]:
            dfs(forward)

        backward = source - arr[source]
        if backward >= 0 and not visited[backward]:
            dfs(backward)

        visited[source] = False

    dfs(start)
    return res["ans"]


# DFS + Optimized Recursive
def can_reach_recursive_optimized(arr: List[int], start: int) -> bool:
    """
    Time Complexity = O(N) ; N = len(arr)
    Space Complexity = O(N) in worst case, N = len(arr) ; To store recursive call in stack
    """
    if start < 0 or start >= len(arr) or arr[start] < 0:
        return False
    arr[start] *= -1
    return arr[start] == 0 \
           or can_reach_recursive_optimized(arr, start + arr[start]) \
           or can_reach_recursive_optimized(arr, start - arr[start])


# DFS + Iterative
def can_reach_iterative(arr: List[int], start: int) -> bool:
    """
   Time Complexity = O(N) ; N = len(arr)
   Space Complexity = O(N); N = len(arr) ; for queue
   """
    q = deque([start])

    while q:
        curr = q.popleft()

        if arr[curr] == 0:
            return True
        if arr[curr] < 0:
            continue
        if arr[curr] + curr < len(arr):
            q.append(arr[curr] + curr)
        if curr - arr[curr] >= 0:
            q.append(curr - arr[curr])

        arr[curr] *= -1

    return False
