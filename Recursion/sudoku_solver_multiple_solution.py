# https://leetcode.com/problems/sudoku-solver/

def is_safe(mat: list, i: int, j: int, no: str, n: int) -> bool:
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
                print(str(mat[i][j]), end=" ")
            print()
        return True

    # rec case
    if j == n:
        return solve_sudoku(mat, i + 1, 0, n)

    # skip the predefined cell
    if mat[i][j] != ".":
        return solve_sudoku(mat, i, j + 1, n)

    # cell to be filled
    # try out all possibilities
    for no in range(1, n + 1):

        if is_safe(mat, i, j, str(no), n):
            mat[i][j] = str(no)
            if solve_sudoku(mat, i, j + 1, n):
                return True

    mat[i][j] = "."


n = 9
matrix = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solve_sudoku(matrix, 0, 0, n)
