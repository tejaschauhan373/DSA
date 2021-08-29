from typing import List


def find_the_left(i, arr: List[int]) -> int:
    depth = 0
    while i - 1 >= 0 and arr[i - 1] < arr[i]:
        depth += 1
        i -= 1
    return depth


def find_the_right(i, arr: List[int]) -> int:
    depth = 0
    while i + 1 < len(arr) and arr[i] > arr[i + 1]:
        depth += 1
        i += 1
    return depth


# Time Complexity : O(N)
# Space Complexity : O(N)
def longestMountain(arr: List[int]) -> int:
    """
    :param arr: list of mountain height
    :return:
    """
    max_length = 0
    for i in range(len(arr) - 2):
        if arr[i] < arr[i + 1] > arr[i + 2]:
            temp = find_the_left(i + 1, arr) + find_the_right(i + 1, arr) + 1
            if max_length < temp:
                max_length = temp

    return max_length
