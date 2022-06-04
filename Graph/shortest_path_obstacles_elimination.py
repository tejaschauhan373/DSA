# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
from collections import deque
from typing import List


def shortest_path_bfs_using_queue(grid: List[List[int]], k: int) -> int:
    """
    Time Complexity = O(R*C*K) ; R = numbers of rows, C = number of columns, K = most k obstacles can remove
    Space Complexity = O(R*C*K)
    """
    R = len(grid)
    C = len(grid[0])

    if k >= R + C - 2: return R + C - 2  # if we can go by manhattan distance -> let's go
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    step = 0
    first_corner = (k, 0, 0)

    seen = {first_corner}
    q = deque([first_corner])

    while q:
        size = len(q)

        while size:
            d, r, c = q.popleft()

            if r == R - 1 and c == C - 1:
                return step

            for k in range(4):
                nx = r + dx[k]
                ny = c + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    new_k = d - grid[nx][ny]
                    new_temp = (new_k, nx, ny)
                    if new_k >= 0 and new_temp not in seen:
                        seen.add(new_temp)
                        q.append(new_temp)

            size -= 1

        step += 1

    return -1
