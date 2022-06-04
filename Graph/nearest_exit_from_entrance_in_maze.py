# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
from collections import deque
from typing import List


def nearest_exit(maze: List[List[str]], entrance: List[int]) -> int:
    grid = maze
    R = len(grid)
    C = len(grid[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[entrance[0]][entrance[1]] = True
    step = 0
    q = deque([entrance])

    while q:
        size = len(q)
        while size:
            r, c = q.popleft()

            if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                if r != entrance[0] or c != entrance[1]:
                    return step

            for k in range(4):
                nx = r + dx[k]
                ny = c + dy[k]
                if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] == "." and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

            size -= 1

        step += 1

    return -1
