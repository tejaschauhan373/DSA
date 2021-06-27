arr = input().split(' ')


def checkReverse(arr, n):
    start = 0
    end = n - 1
    for i in range(n // 2):
        if arr[start] != arr[end]:
            return False
    return True


print(checkReverse(arr, len(arr)))
