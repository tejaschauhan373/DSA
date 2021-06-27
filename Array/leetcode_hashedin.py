def horizontal(grid, j, i, h, w, check):
    if i - 1 >= 0:
        if grid[j][i - 1] == check:
            grid[j][i - 1] = 2
            horizontal(grid, j, i - 1, h, w, check)

    if j - 1 >= 0:
        if grid[j - 1][i] == check:
            grid[j - 1][i] = 2
            horizontal(grid, j - 1, i, h, w, check)

    if j + 1 < h:
        if grid[j + 1][i] == check:
            grid[j + 1][i] = 2
            horizontal(grid, j + 1, i, h, w, check)

    if i + 1 < w:
        if grid[j][i + 1] == check:
            grid[j][i + 1] = 2
            horizontal(grid, j, i + 1, h, w, check)


def numIslands(grid) -> int:
    h = len(grid)
    w = len(grid[0])
    count = 0
    for j in range(h):
        for i in range(w):
            if grid[j][i] == '1':
                print(j, i)
                horizontal(grid, j, i, h, w, "1")
                count += 1
    return count


print(numIslands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]]))
