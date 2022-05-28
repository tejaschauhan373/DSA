# https://www.udemy.com/course/cpp-data-structures-algorithms-levelup-prateek-narang/learn/lecture/26187768#overview
# BFS + Dijkstra Algorithm (Shortest Path)

matrix = [
    [31, 100, 65, 12, 18],
    [10, 13, 47, 157, 6],
    [100, 113, 174, 11, 33],
    [88, 124, 41, 20, 140],
    [99, 32, 111, 41, 20]
]


# BFS recursive
def shortest_path_recursive(grid: list, visited_place: list, res: int, i, j, R, C):
    """
    Time Complexity = O(N) ; Number of cells in matrix (to traverse through each node)
    Space Complexity = O(N) ; Number of cells in matrix (to keep track of visited place)
    """
    if i == R - 1 and j == C - 1:
        return res + grid[i][j]

    res += grid[i][j]
    visited_place[i][j] = True
    # up, left, down, right (anti clock wise)
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, -1, 0, 1]

    min_val = float("+inf")

    route = []
    for k in range(4):
        next_x = dir_x[k] + i
        next_y = dir_y[k] + j

        if 0 <= next_x < R and 0 <= next_y < C and not visited_place[next_x][next_y]:
            if grid[next_x][next_y] == min_val:
                min_val = grid[next_x][next_y]
                route.append([next_x, next_y])
            elif grid[next_x][next_y] < min_val:
                min_val = grid[next_x][next_y]
                route = [[next_x, next_y]]

    if min_val != float("+inf"):
        multiple_route_res = []
        for min_x, min_y in route:
            multiple_route_res.append(shortest_path_recursive(grid, visited_place, res, min_x, min_y, R, C))
        return min(multiple_route_res)
    else:
        return float("+inf")


class Node:

    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


# BFS iterative
def shortest_path_iterative(grid: list, rows: int, columns: int):
    i = 0
    j = 0

    distance = [[float("+inf") for _ in range(columns)] for _ in range(rows)]

    distance[i][j] = grid[0][0]

    q = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q.append(Node(0, 0, distance[0][0]))

    while q:
        curr = q.pop(0)
        cx = curr.x
        cy = curr.y
        cd = curr.dist

        # update neighbours
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if 0 <= nx < rows and 0 <= ny < columns and cd + grid[nx][ny] < distance[nx][ny]:
                # Remove the old node if it exist
                node = Node(nx, ny, distance[nx][ny])
                try:
                    q.remove(node)
                except ValueError:
                    pass

                # insert the new node in the set
                nd = grid[nx][ny] + cd
                distance[nx][ny] = nd
                q.append(Node(nx, ny, distance[nx][ny]))

        q = sorted(q, key=lambda x: x.dist)

    return distance[rows - 1][columns - 1]


R = len(matrix)
C = len(matrix[0])

visited = [[False for _ in range(C)] for _ in range(R)]

print(shortest_path_recursive(matrix, visited, 0, 0, 0, R, C))
print(shortest_path_iterative(matrix, R, C))
