# https://leetcode.com/problems/is-graph-bipartite
from typing import List
from collections import defaultdict, deque


# DFS
def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Time Complexity = O(V+E)
    Space Complexity = O(V+E) in worst case if each node connected to every other nodes of graph
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

    n = len(graph)
    if n == 1 or not graph:
        return True

    dislike_graph = defaultdict(set)
    color_table = defaultdict(int)

    for node, nbrs in enumerate(graph):
        for nbr in nbrs:
            dislike_graph[node].add(nbr)
            dislike_graph[nbr].add(node)

    for node in range(n):
        if color_table[node] == NOT_COLORED and (not helper(node, BLUE)):
            return False

    return True


# BFS
def possible_bi_partition(n: int, dislikes: List[List[int]]) -> bool:
    """
    Time Complexity = O(V+E)
    Space Complexity = O(V+E) in worst case if each node connected to every other nodes of graph
    ; V = no. of vertices, E = no. of edges
    """
    if n == 1:
        return True

    graph = defaultdict(set)
    for node, nbr in dislikes:
        graph[nbr].add(node)
        graph[node].add(nbr)

    color_table = defaultdict(int)
    i = 1
    while i < n + 1:
        if color_table[i] == 0:
            q = deque([[i, 1]])
            while q:
                size = len(q)
                while size:
                    node, color = q.popleft()
                    color_table[node] = color
                    for nbr in graph[node]:
                        if color_table[nbr] == color:
                            return False
                        if color_table[nbr] == 0:
                            q.append([nbr, -color])
                    size -= 1
        i += 1
    return True
