from typing import List


def binary_search(arr: list, l, r, x, divi):
    print("left", l, "right", r)

    if r >= l:

        mid = l + (r - l) // 2

        print(mid // divi, mid % divi)

        mid_ele = arr[mid // divi][mid % divi]

        if mid_ele == x:
            return mid
        elif mid_ele > x:
            return binary_search(arr, l, mid - 1, x, divi)
        else:
            return binary_search(arr, mid + 1, r, x, divi)
    else:
        return -1


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False

    height = len(matrix)
    width = len(matrix[0])

    low = 0
    high = (height * width) - 1

    m = len(matrix[0])
    while low <= high:

        mid = low + (high - low) // 2

        if matrix[mid // m][mid % m] == target:
            return True

        if matrix[mid // m][mid % m] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
