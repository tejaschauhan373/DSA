# https://leetcode.com/problems/possible-bipartition/
from collections import defaultdict, deque
from typing import List


# DFS
def possible_bi_partition(n: int, dislikes: List[List[int]]) -> bool:
    """
    Time Complexity = O(V+E)
    Space Complexity = O(V+E)
    ; V = no. of vertices, E = no. of edges
    """
    NOT_COLORED, BLUE, GREEN = 0, 1, -1

    def helper(person_id, color):
        color_table[person_id] = color

        for the_other in dislike_graph[person_id]:
            if color_table[the_other] == color: return False

            if color_table[the_other] == NOT_COLORED and (not helper(the_other, -color)):
                return False
        return True

    if n == 1 or not dislikes:
        return True

    dislike_graph = defaultdict(list)
    color_table = defaultdict(int)

    for src, dest in dislikes:
        dislike_graph[src].append(dest)
        dislike_graph[dest].append(src)

    for node in range(1, n + 1):
        if color_table[node] == NOT_COLORED and (not helper(node, BLUE)):
            return False

    return True


# BFS
def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Time Complexity = O(V+E)
    Space Complexity = O(V+E)
    ; V = no. of vertices, E = no. of edges
    """
    n = len(graph)
    if n == 1:
        return True

    color_table = defaultdict(int)
    visited = [0] * n
    i = 0
    while i < n:
        if not visited[i]:
            q = deque([[i, 1]])
            while q:
                size = len(q)
                while size:
                    node, color = q.popleft()
                    color_table[node] = color
                    visited[node] = True
                    for nbr in graph[node]:
                        if color_table[nbr] == color:
                            return False
                        if not visited[nbr]:
                            q.append([nbr, -color])
                    size -= 1
        i += 1
    return True
