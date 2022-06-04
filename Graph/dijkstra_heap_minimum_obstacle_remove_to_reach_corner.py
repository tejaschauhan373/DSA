# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
from heapq import *
from typing import List, Union, Any
from math import inf


def minimum_obstacles(grid: List[List[int]]) -> Union[float, Any]:
    R = len(grid)
    C = len(grid[0])
    dist = [[inf for _ in range(C)] for _ in range(R)]
    dist[0][0] = grid[0][0]
    hp = []
    heappush(hp, (dist[0][0], 0, 0))

    while hp:
        d, r, c = heappop(hp)
        if r == R - 1 and c == C - 1:
            return d
        else:
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for k in range(4):
                nx = r + dx[k]
                ny = c + dy[k]
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] + d < dist[nx][ny]:
                    dist[nx][ny] = d + grid[nx][ny]
                    heappush(hp, (dist[nx][ny], nx, ny))
    return dist[-1][-1]
