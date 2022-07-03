# https://leetcode.com/problems/jump-game-iv/
from typing import List
from collections import defaultdict, deque


def min_jumps_recursive_brute_force(arr: List[int]) -> int:
    """
    Time Complexity = O(k^N); k = neighbour nodes, N = len(arr)
    Space Complexity = O(N) ; N = len(arr)
    """
    res = {"ans": float("+inf")}
    visited = [False] * len(arr)

    def jump(i, steps):
        nonlocal res, visited
        if i == len(arr) - 1:
            res["ans"] = min(res["ans"], steps)
            return

        visited[i] = True

        if i + 1 < len(arr) and not visited[i + 1]:
            jump(i + 1, steps + 1)

        if i - 1 >= 0 and not visited[i - 1]:
            jump(i - 1, steps + 1)

        temp = i + 1
        while temp < len(arr):
            if arr[temp] == arr[i]:
                if not visited[temp]:
                    jump(temp, steps + 1)
            temp += 1

        visited[i] = False

    jump(0, 0)
    return res["ans"]


def min_jumps_most_optimized_bfs(arr: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    ; N = len(arr)
    """
    n = len(arr)
    if n <= 1:
        return 0

    graph = defaultdict(list)
    for i in range(n):
        graph[arr[i]].append(i)

    curs = deque([0])  # store current layers
    visited = {0}
    step = 0

    # when current layer exists
    while curs:
        size = len(curs)

        # iterate the layer
        while size:
            node = curs.popleft()
            if node == n - 1:
                return step

            # check same value
            for child in graph[arr[node]]:
                if child not in visited:
                    visited.add(child)
                    curs.append(child)

            # clear the list to prevent redundant search
            graph[arr[node]].clear()

            # check neighbors
            for child in [node - 1, node + 1]:
                if 0 <= child < len(arr) and child not in visited:
                    visited.add(child)
                    curs.append(child)

            size -= 1

        step += 1

    return -1
