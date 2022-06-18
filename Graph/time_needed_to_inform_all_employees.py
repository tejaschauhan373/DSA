# https://leetcode.com/problems/time-needed-to-inform-all-employees
from collections import defaultdict, deque
from typing import List
from heapq import *


def num_of_minutes_bfs_queue(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    ; N = number of nodes
    """
    graph = defaultdict(set)
    for i, v in enumerate(manager):
        graph[v].add(i)

    level = deque([(headID, informTime[headID])])
    cost = 0
    while level:
        size = len(level)
        while size:
            node, time = level.popleft()
            cost = max(cost, time)
            for nbr in graph[node]:
                level.append((nbr, time + informTime[nbr]))
            size -= 1

    return cost


def num_of_minutes__dijkstra_heapq(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    ; N = number of nodes
    """
    graph = defaultdict(set)
    for i, v in enumerate(manager):
        graph[v].add(i)

    level = [(informTime[headID], headID)]
    distance = [0] * n
    while level:
        size = len(level)
        while size:
            time, node = heappop(level)
            distance[node] = time
            for nbr in graph[node]:
                heappush(level, (time + informTime[nbr], nbr))
            size -= 1

    return max(distance)


def num_of_minutes_dfs_recursive(n: int, headID: int, manager: List[int], informTime: List[int]):
    """
    Time Complexity = O(N)
    Space Complexity = O(N) ; To store recursive call stack
    ; N = number of nodes
    """

    graph = defaultdict(set)
    for i, v in enumerate(manager):
        graph[v].add(i)
    res = 0

    def dfs(manager, time):
        nonlocal res
        nonlocal informTime
        res = max(res, time)
        for nbr in graph[manager]:
            dfs(nbr, time + informTime[nbr])

    dfs(headID, informTime[headID])
    return res
