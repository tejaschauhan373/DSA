# N queen problem

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()


def can_place(board: list, i: int, j: int):
    # find diagonally
    temp_i, temp_j = i - 1, j - 1
    while temp_i > -1 and temp_j > -1:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i -= 1
        temp_j -= 1

    temp_i, temp_j = i - 1, j + 1
    while temp_i > -1 and temp_j < len(board):
        if board[temp_i][temp_j] == 1:
            return False
        temp_i -= 1
        temp_j += 1

    temp_i, temp_j = i + 1, j - 1
    while temp_i < len(board) and temp_j > -1:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i += 1
        temp_j -= 1

    temp_i, temp_j = i + 1, j + 1
    while temp_i < len(board) and temp_j < len(board):
        if board[temp_i][temp_j] == 1:
            return False
        temp_i += 1
        temp_j += 1

    # find horizontally
    temp_i, temp_j = i, j + 1
    while temp_j < len(board):
        if board[temp_i][temp_j] == 1:
            return False
        temp_j += 1

    temp_i, temp_j = i, j - 1
    while temp_j > -1:
        if board[temp_i][temp_j] == 1:
            return False
        temp_j -= 1

    # find vertically
    temp_i, temp_j = i + 1, j
    while temp_i < len(board):
        if board[temp_i][temp_j] == 1:
            return False
        temp_i += 1

    temp_i, temp_j = i - 1, j
    while temp_i > -1:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i -= 1

    return True


def solve_n_queen(n: int, board: list, i: int):
    if i == n:
        print_board(board)
        return True

    for j in range(n):

        if can_place(board, i, j):
            board[i][j] = 1
            success = solve_n_queen(n, board, i + 1)
            if success:
                return True

            board[i][j] = 0

    return False


n = 4

my_board = [[0 for i in range(n)] for j in range(n)]

print(solve_n_queen(4, my_board, 0))
