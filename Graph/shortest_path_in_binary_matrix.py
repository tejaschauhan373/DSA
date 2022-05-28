# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque
from typing import List


# Array + Matrix + BFS
def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    Time Complexity = O(N) ; N = Number of cells
    Space Complexity = O(N) ; N = Number of cells
    """

    if grid[0][0] == 1:
        return -1

    matrix = grid
    R = len(matrix)
    C = len(matrix[0])
    visited = [[False for _ in range(C)] for _ in range(R)]

    q = deque()
    q.append(tuple([0, 0]))
    visited[0][0] = True

    dir_x = [-1, 0, 1, 0, 1, 1, -1, -1]
    dir_y = [0, -1, 0, 1, -1, 1, -1, 1]
    level = 0
    while q:

        size = len(q)
        level += 1
        while size:
            i, j = q.popleft()
            visited[i][j] = True

            if i == R - 1 and j == C - 1:
                return level
            for k in range(8):
                next_x = dir_x[k] + i
                next_y = dir_y[k] + j

                if 0 <= next_x < R and 0 <= next_y < C:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        temp = tuple([next_x, next_y])
                        if temp not in q:
                            q.append(temp)

            size -= 1

    return -1
