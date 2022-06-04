# https://leetcode.com/problems/shortest-bridge/
from collections import deque
from typing import List


def shortest_bridge(grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])

    def get_first_island_point():
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return [i, j]

    stack = [get_first_island_point()]
    if stack[0] is None:
        return 0
    boundaries = deque()

    while stack:
        i, j = stack.pop()

        grid[i][j] = -1

        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, 1, -1]
        for k in range(4):
            cx = i + dir_x[k]
            cy = j + dir_y[k]
            if 0 <= cx < R and 0 <= cy < C:
                if grid[cx][cy] == 1:
                    stack.append([cx, cy])
                    grid[cx][cy] = -1
                elif grid[cx][cy] == 0:
                    grid[cx][cy] = -1
                    boundaries.append([cx, cy])

    step = 0
    while boundaries:
        size = len(boundaries)
        step += 1

        while size:
            i, j = boundaries.popleft()
            grid[i][j] = -1

            dir_x = [1, -1, 0, 0]
            dir_y = [0, 0, 1, -1]
            for k in range(4):
                cx = i + dir_x[k]
                cy = j + dir_y[k]
                if 0 <= cx < R and 0 <= cy < C:
                    if grid[cx][cy] == 1:
                        return step
                    elif grid[cx][cy] == 0:
                        grid[cx][cy] = -1
                        boundaries.append([cx, cy])
            size -= 1

    return -1
