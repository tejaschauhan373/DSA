# https://leetcode.com/problems/sudoku-solver/

def is_safe(mat: list, i: int, j: int, no: int, n: int) -> bool:
    # Check for row and col
    for k in range(n):
        if mat[k][j] == no or mat[i][k] == no:
            return False

    # Check for subgrid

    sx = (i // 3) * 3
    sy = (j // 3) * 3

    for x in range(sx, sx + 3):
        for y in range(sy, sy + 3):
            if mat[x][y] == no:
                return False

    return True


def solve_sudoku(mat: list, i: int, j: int, n: int):
    # base case
    if i == n:

        for i in range(n):
            for j in range(n):
                print(mat[i][j], end=" ")
            print()
        return True

    # rec case
    if j == n:
        return solve_sudoku(mat, i + 1, 0, n)

    # skip the predefined cell
    if mat[i][j] != 0:
        return solve_sudoku(mat, i, j + 1, n)

    # cell to be filled
    # try out all possibilities
    for no in range(1, n + 1):

        if is_safe(mat, i, j, no, n):
            mat[i][j] = no
            solve_problem = solve_sudoku(mat, i, j + 1, n)
            if solve_problem:
                return True

    mat[i][j] = 0
    return False


n = 9
matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(matrix, 0, 0, n)
