def horizontal(grid, j, i, h, w, check):
    count = 0
    if i - 1 >= 0:
        if grid[j][i - 1] == check:
            count += 1
            grid[j][i - 1] = 2
            count += horizontal(grid, j, i - 1, h, w, check)

    if j - 1 >= 0:
        if grid[j - 1][i] == check:
            count += 1
            grid[j - 1][i] = 2
            count += horizontal(grid, j - 1, i, h, w, check)

    if j + 1 < h:
        if grid[j + 1][i] == check:
            count += 1
            grid[j + 1][i] = 2
            count += horizontal(grid, j + 1, i, h, w, check)

    if i + 1 < w:
        if grid[j][i + 1] == check:
            count += 1
            grid[j][i + 1] = 2
            count += horizontal(grid, j, i + 1, h, w, check)

    return count


def numIslands(grid) -> int:
    h = len(grid)
    w = len(grid[0])
    max = 0
    # if h == 1 and w == 1:
    #     return int(grid[0][0] == 1)
    for j in range(h):
        for i in range(w):
            if grid[j][i] == 1:
                result = horizontal(grid, j, i, h, w, 1)
                if max == 0:
                    max += 1
                elif result > max:
                    max = result

    return max


print(numIslands([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

print(numIslands([[0, 0, 0, 0, 0, 0, 0, 0]]))

print(numIslands([[1, 1, 0, 1, 1],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [1, 1, 0, 1, 1]]))

print(numIslands([[1]]))

print(numIslands([[0, 1]]))
print(numIslands([[1, 0, 1]]))
