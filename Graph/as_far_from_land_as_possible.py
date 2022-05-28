# https://leetcode.com/problems/as-far-from-land-as-possible/
from collections import deque
from typing import List


# Array + DFS
def max_distance(grid: List[List[int]]) -> int:
    """
    Time Complexity = O(N*M) ; N = number of rows, M = number of columns
    Space Complexity = O(N*M) ; N = number of rows, M = number of columns
    """

    R = len(grid)
    C = len(grid[0])

    # Direction matrix (from up then clockwise (up-left-down-right))
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, -1, 0, 1]

    q = deque()

    # Store all land coordinates in queue
    for i in range(R):
        for j in range(C):
            if grid[i][j]:
                q.append(tuple([i, j]))

    # If matrix has no water then ans is -1
    if len(q) == R * C:
        return -1

    dist = 0

    # Standard BFS
    while q:

        dist += 1

        size = len(q)

        while size:
            ci, cj = q.popleft()

            # pushing all coordinates of land
            for i in range(4):
                new_x = ci + dir_x[i]
                new_y = cj + dir_y[i]

                if 0 <= new_x < R and 0 <= new_y < C:
                    if grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = 1
                        q.append(tuple([new_x, new_y]))
            size -= 1

    return dist - 1
