# https://leetcode.com/problems/snakes-and-ladders
from typing import List
from collections import deque


# BFS
def snake_and_ladders(board: List[List[int]]) -> int:
    # BFS solution - Since its BFS it will find the path with least steps

    n = len(board)

    # Compute the indices in the array of the square
    def compute_index(square):
        # Compute quotient (r) and remainder (c) of square - 1/ n
        r, c = divmod(square - 1, n)

        # The order (left - right or left - right) that the numbers increases
        if r % 2 == 0:
            # Calculating the indices ([n][0] is square 1)
            return n - 1 - r, c
        else:
            return n - 1 - r, n - 1 - c

    visited = set()
    queue = deque([])
    queue.append((1, 0))  # 1 is position in chess board, 0 as total step

    while queue:
        curr_square, step_num = queue.popleft()
        r, c = compute_index(curr_square)

        # There is a snake or ladder
        if board[r][c] != -1:
            curr_square = board[r][c]

        # Reached the last square, return the step number
        if curr_square == n * n:
            return step_num

        # All possible future steps (next 6 squares) that are less than n*n, the last square
        for new_square in range(curr_square + 1, min(curr_square + 6, n * n) + 1):
            # Ensure no cycles
            if new_square not in visited:
                # Add to set
                visited.add(new_square)
                queue.append((new_square, step_num + 1))

    return -1


board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]
]

print(snake_and_ladders(board))
