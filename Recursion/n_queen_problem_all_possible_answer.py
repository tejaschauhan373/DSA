# N queen problem
# https://leetcode.com/problems/n-queens/submissions/
def print_board(board, answer: list):
    temp_answer = []
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            if board[i][j] == 0:
                row += "."
            else:
                row += "Q"
        temp_answer.append(row)
    answer.append(temp_answer)


def can_place(board: list, i: int, j: int, n: int):
    # find diagonally
    temp_i, temp_j = i - 1, j - 1
    while temp_i > -1 and temp_j > -1:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i -= 1
        temp_j -= 1

    temp_i, temp_j = i - 1, j + 1
    while temp_i > -1 and temp_j < n:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i -= 1
        temp_j += 1

    temp_i, temp_j = i + 1, j - 1
    while temp_i < n and temp_j > -1:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i += 1
        temp_j -= 1

    temp_i, temp_j = i + 1, j + 1
    while temp_i < n and temp_j < n:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i += 1
        temp_j += 1

    # find horizontally
    temp_i, temp_j = i, j + 1
    while temp_j < n:
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
    while temp_i < n:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i += 1

    temp_i, temp_j = i - 1, j
    while temp_i > -1:
        if board[temp_i][temp_j] == 1:
            return False
        temp_i -= 1

    return True


def solve_n_queen(n: int, board: list, i: int, answer: list):
    if i == n:
        print_board(board, answer)
        return

    for j in range(n):

        if can_place(board, i, j, n):
            board[i][j] = 1
            solve_n_queen(n, board, i + 1, answer)
            board[i][j] = 0


n = 4
answer = []
my_board = [[0 for i in range(n)] for j in range(n)]

print(solve_n_queen(4, my_board, 0, answer))
print(answer)
