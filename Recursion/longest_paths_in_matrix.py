# https://practice.geeksforgeeks.org/problems/longest-path-in-a-matrix3019
# Python3 program to find the longest path in a Matrix
# with given constraints

n = 3


# Returns length of the longest path beginning with mat[i][j].
# This function mainly uses lookup table dp[n][n]
def find_longest_from_a_cell(i, j, mat, dp, row, column):
    # Base case
    if i < 0 or i >= row or j < 0 or j >= column:
        return 0

    # If this sub problem is already solved
    if dp[i][j] != -1:
        return dp[i][j]

    # To store the path lengths in all the four directions
    x, y, z, w = -1, -1, -1, -1

    # Since all numbers are unique and in range from 1 to n * n,
    # there is at most one possible direction from any cell
    # Right
    if j < column - 1 and ((mat[i][j] + 1) <= mat[i][j + 1]):
        x = 1 + find_longest_from_a_cell(i, j + 1, mat, dp, row, column)

    # Left
    if j > 0 and (mat[i][j] + 1 <= mat[i][j - 1]):
        y = 1 + find_longest_from_a_cell(i, j - 1, mat, dp, row, column)

    # Up
    if i > 0 and (mat[i][j] + 1 <= mat[i - 1][j]):
        z = 1 + find_longest_from_a_cell(i - 1, j, mat, dp, row, column)

    # Down
    if i < row - 1 and (mat[i][j] + 1 <= mat[i + 1][j]):
        w = 1 + find_longest_from_a_cell(i + 1, j, mat, dp, row, column)

    # If none of the adjacent fours is one greater we will take 1
    # otherwise we will pick maximum from all the four directions
    dp[i][j] = max(x, y, z, w, 1)
    return dp[i][j]


# Returns length of the longest path beginning with any cell
def fin_longest_over_all(mat):
    result = 1  # Initialize result

    # Create a lookup table and fill all entries in it as -1
    dp = [[-1 for i in range(n)] for i in range(n)]

    row = len(mat)
    column = len(mat[0])
    # Compute longest path beginning from all cells
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                find_longest_from_a_cell(i, j, mat, dp, row, column)
            # Update result if needed
            result = max(result, dp[i][j])

    print(dp)
    return result


# Driver program
mat = [[1, 2, 9],
       [5, 3, 8],
       [4, 6, 7]]
print("Length of the longest path is ", fin_longest_over_all(mat))
