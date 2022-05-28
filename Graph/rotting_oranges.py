# https://leetcode.com/problems/rotting-oranges/
from typing import List
from collections import deque


# Array + BFS + Queue + Matrix
def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Time Complexity = O(N*M) -> Each cell will be visited at least once
    Space Complexity = O(N*M) (in the worst case if all the oranges are rotten they will be added to the queue)
    ; N = number of rows, M = number of columns
    """
    R = len(grid)
    C = len(grid[0])

    rotten = deque()

    dir_x = [-1, 0, 1, 0]
    dir_y = [0, 1, 0, -1]

    fresh_orange_count = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                fresh_orange_count += 1
            elif grid[i][j] == 2:
                rotten.append([i, j])

    if fresh_orange_count == 0:
        return 0

    minutes = 0

    while rotten:
        minutes += 1
        size = len(rotten)

        while size:

            x, y = rotten.popleft()

            for j in range(4):
                cx = x + dir_x[j]
                cy = y + dir_y[j]

                if 0 <= cx < R and 0 <= cy < C:
                    if grid[cx][cy] == 1:
                        grid[cx][cy] = 2
                        fresh_orange_count -= 1
                        rotten.append([cx, cy])
            size -= 1

    if fresh_orange_count == 0:
        return minutes - 1
    else:
        return -1
