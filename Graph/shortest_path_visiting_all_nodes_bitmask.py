# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/178744/Python-BFS-solution-with-optimization.-Beats-100

from math import inf
from collections import deque


def shortest_path_length(graph):
    node_count = len(graph)
    masks = [1 << i for i in range(node_count)]
    all_visited = (1 << node_count) - 1
    queue = deque([(i, masks[i]) for i in range(node_count)])
    steps = 0

    visited_states = [{masks[i]} for i in range(node_count)]

    while queue:
        count = len(queue)

        while count:
            current_node, visited = queue.popleft()
            if visited == all_visited:
                return steps
            for nb in graph[current_node]:
                new_visited = visited | masks[nb]
                if new_visited == all_visited:
                    return steps + 1
                if new_visited not in visited_states[nb]:
                    visited_states[nb].add(new_visited)
                    queue.append((nb, new_visited))
            count -= 1
        steps += 1
    return inf
