arr = list(map(int, input().split(' ')))


def rotate(arr, n):
    x = arr[-1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x


rotate(arr, len(arr))

print(arr)
