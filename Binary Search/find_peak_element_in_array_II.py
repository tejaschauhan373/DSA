# https://leetcode.com/problems/find-a-peak-element-ii/
# https://www.youtube.com/watch?v=HtSuA80QTyo
from typing import List


def find_peak_grid_brute(mat: List[List[int]]) -> List[int]:
    r = len(mat)
    c = len(mat[0])
    for i in range(r):
        for j in range(c):
            if i - 1 > -1 and mat[i - 1][j] > mat[i][j]:
                continue
            elif j - 1 > -1 and mat[i][j - 1] > mat[i][j]:
                continue
            elif i + 1 < r and mat[i + 1][j] > mat[i][j]:
                continue
            elif j + 1 < c and mat[i][j + 1] > mat[i][j]:
                continue
            else:
                return [i, j]


def find_peak_grid_optimal(mat: List[List[int]]) -> List[int]:
    start_col = 0
    end_col = len(mat[0]) - 1

    while start_col <= end_col:
        max_row = 0
        mid_col = (end_col + start_col) // 2

        for row in range(len(mat)):
            if mat[row][mid_col] >= mat[max_row][mid_col]:
                max_row = row

        if mid_col - 1 >= start_col and mat[max_row][mid_col - 1] > mat[max_row][mid_col]:
            end_col = mid_col - 1
        elif mid_col + 1 <= end_col and mat[max_row][mid_col + 1] > mat[max_row][mid_col]:
            start_col = mid_col + 1
        else:
            return [max_row, mid_col]
    return []
