arr = list(map(int, input().split(' ')))


def min_jumps(arr, n):
    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1
    max_reach = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1, n):
        if i == n - 1:
            return jump
        max_reach = max(max_reach, i + arr[i])

        step -= 1
        if step == 0:
            jump += 1

            if i >= max_reach:
                return -1

            step = max_reach - i
            print("i", i, "step", step)
    return -1


print(min_jumps(arr, len(arr)))
