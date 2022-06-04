# https://leetcode.com/problems/all-paths-from-source-to-target/
from collections import defaultdict
from typing import List


class DirectedGraph:

    def __init__(self):
        self.vertices = defaultdict(set)

    def add_edge(self, i: int, j):
        if j is not None:
            self.vertices[i].add(j)
        elif i not in self.vertices:
            self.vertices[i] = set()

    def total_v(self):
        self.total_vertices = len(self.vertices)

    def dfs_to_dest_recusrive(self, source, dest, stack, res, curr):
        # Arrive Node
        stack[source] = True
        new_curr = curr.copy()
        new_curr.append(source)

        # Do some work at node, return True if backedge is found here itself
        for nbr in self.vertices[source]:
            if not stack[nbr]:
                if nbr == dest:
                    res.append(new_curr + [nbr])
                else:
                    self.dfs_to_dest_recusrive(nbr, dest, stack, res, new_curr)

        # going back
        stack[source] = False

    def get_all_path_from_source_to_dest(self, source, dest):
        stack = [False] * self.total_vertices
        res = []
        self.dfs_to_dest_recusrive(source, dest, stack, res, [])
        return res

    def dfs_to_dest_with_stack(self, source, dest):
        # apply DFS on DAG
        stack = [(source, [source])]  # - store noth the (node, and the path leading to it)
        res = []
        while stack:
            node, path = stack.pop()
            # check leaf
            if node == dest:
                res.append(path)
            # traverse rest
            for nei in self.vertices[node]:
                stack.append((nei, path + [nei]))
        return res


def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    g = DirectedGraph()
    for i, temp in enumerate(graph):
        if temp:
            for nbr in temp:
                g.add_edge(i, nbr)
        else:
            g.add_edge(i, None)

    g.total_v()
    dest = g.total_vertices - 1
    res = g.get_all_path_from_source_to_dest(0, dest)
    return res
