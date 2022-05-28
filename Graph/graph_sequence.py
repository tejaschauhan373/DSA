# DFS + DP
# longest increasing sequence

# Time Complexity = O(N); Number of cells
# Space Complexity = O(N); To store value in DP array
def dfs(matrix: list, visited: list, cache: list, i: int, j: int):
    visited[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] > matrix[i][j]:
            if not visited[nx][ny]:
                dfs(matrix, visited, cache, nx, ny)
            cnt = max(cnt, 1 + cache[nx][ny])

    cache[i][j] = cnt
    return


matrix = [
    [0, 2, 4, 3, 2],
    [7, 6, 5, 5, 1],
    [8, 9, 7, 18, 14],
    [5, 10, 11, 12, 13]
]

R = len(matrix)
C = len(matrix[0])

visited = [[False for _ in range(C)] for _ in range(R)]
cache = [[0 for _ in range(C)] for _ in range(R)]
max_length = float("-inf")
for i in range(R):
    for j in range(C):
        dfs(matrix, visited, cache, i, j)
        max_length = max(max_length, matrix[i][j])

print(cache)
print(max_length)
