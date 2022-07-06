arr = input().split(' ')


def checkReverse(arr, n):
    """
    Time Complexity = O(n/2)
    Space Complexity = O(1)
    """
    end = n - 1
    for i in range(n // 2):
        if arr[i] != arr[end - i]:
            return False
    return True


print(checkReverse(arr, len(arr)))
