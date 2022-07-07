# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
from typing import List


def find_min_binary_search(nums: List[int]) -> int:
    """
    Time Complexity = O(log(N)) ; N = len(nums)
    Space Complexity = O(1)
    """
    if len(nums) == 1:
        return nums[0]

    start = 0
    end = len(nums) - 1

    if nums[end] > nums[0]:
        return nums[0]

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[mid] > nums[0]:
            start = mid + 1
        else:
            end = mid - 1


def find_min_binary_search_concise(nums: List[int]) -> int:
    """
    Time Complexity = O(log(N)) ; N = len(nums)
    Space Complexity = O(1)
    """
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[start]:
            end = mid
            start += 1
        else:
            end -= 1
    return nums[start]
