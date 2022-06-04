# https://leetcode.com/problems/count-servers-that-communicate
from typing import List


def count_servers_brute(grid: List[List[int]]) -> int:
    """
    Time Complexity in worst case = O(N*M*max(N, M))
    Space Complexity = O(N*M)
    ; N = number of rows, M = number of columns
    """
    R = len(grid)
    C = len(grid[0])
    visited = [[False for _ in range(C)] for _ in range(R)]
    res = 0
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and grid[i][j]:
                count = 0
                stack = [[i, j]]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    count += 1
                    for p in range(R):
                        if grid[p][y] and not visited[p][y]:
                            visited[p][y] = True
                            stack.append([p, y])
                    for q in range(C):
                        if grid[x][q] and not visited[x][q]:
                            visited[x][q] = True
                            stack.append([x, q])
                if count > 1:
                    res += count
    return res


def count_servers_optimal_complex_to_understand(grid):
    """
    Time Complexity = O(N*M)
    Space Complexity = max(N + M)
    ; N = number of rows, M = number of columns
    """
    X, Y = list(map(sum, grid)), list(map(sum, zip(*grid)))
    return sum(X[i] + Y[j] > 2 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])


def count_servers(grid):
    """
    Time Complexity = O(N*M)
    Space Complexity = max(N + M)
    ; N = number of rows, M = number of columns
    """
    rows = grid[0]
    cols = len(grid[0])

    # Check the input: size of the grid. If it is 0 then exit
    if not (cols and rows):
        return 0

    connected = 0  # Store the number of connected computers
    points = []  # Store coordinates of all the computers
    comps_per_row = [0] * rows  # Store number of computers in given row
    comps_per_col = [0] * cols  # Store number of computers in given column

    for row_i in range(rows):
        for col_i in range(cols):
            if grid[row_i][col_i]:  # Checking if given cell is not 0
                points.append((row_i, col_i))  # add coordinated to the set
                comps_per_row[row_i] += 1  # increase number of computers in a given row
                comps_per_col[col_i] += 1  # increase number of computers in a given column

    # Iterate through all computers
    for row_i, col_i in points:
        # is there more than 1 computer in given row or column
        if comps_per_row[row_i] > 1 or comps_per_col[col_i] > 1:
            # if yes, then computer is connected, count him
            connected += 1

    return connected
