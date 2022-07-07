# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
from typing import List


def find_min_binary_search(nums: List[int]) -> int:
    """
    Time Complexity = O(N) ; N = len(nums)
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
