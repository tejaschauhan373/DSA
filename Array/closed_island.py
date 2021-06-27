def horizontal(grid, j, i, h, w, check):
    result = True
    if i - 1 >= 0:
        if grid[j][i - 1] == check:
            if i - 1 == 0:
                result = False
            grid[j][i - 1] = 2
            result1 = horizontal(grid, j, i - 1, h, w, check)
            if result:
                result = result1


    if j - 1 >= 0:
        if grid[j - 1][i] == check:
            if j - 1 == 0:
                result = False
            grid[j - 1][i] = 2
            result2 = horizontal(grid, j - 1, i, h, w, check)
            if result:
                result = result2

    if j + 1 < h:
        if grid[j + 1][i] == check:
            if j + 1 == h - 1:
                result = False
            grid[j + 1][i] = 2
            result3 = horizontal(grid, j + 1, i, h, w, check)
            if result:
                result = result3
                # result = False

    if i + 1 < w:
        if grid[j][i + 1] == check:
            if i + 1 == w - 1:
                result = False
            grid[j][i + 1] = 2
            result4 = horizontal(grid, j, i + 1, h, w, check)
            if result:
                result = result4

    return result


def numIslands(grid) -> int:
    h = len(grid)
    w = len(grid[0])
    count = 0
    for j in range(1, h - 1):
        for i in range(1, w - 1):
            if grid[j][i] == 0:
                if horizontal(grid, j, i, h, w, 0):
                    print("j",j ,"i", i)
                    count += 1
    return count


print(numIslands(
    [[1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1]]))

print(numIslands(
    [[1, 1, 1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 1, 1, 0],
     [1, 0, 1, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0]]))

print(numIslands([[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                  [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                  [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                  [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                  [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                  [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]))
