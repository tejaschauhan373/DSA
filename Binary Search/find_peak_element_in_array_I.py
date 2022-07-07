# https://leetcode.com/problems/find-peak-element/
# https://www.youtube.com/watch?v=HtSuA80QTyo
from typing import List


def find_peak_element_brute(nums: List[int]) -> int:
    """
    Time Complexity = O(N) ; N = no. of elements in array
    Space Complexity = O(1)
    """
    i = 1
    n = len(nums)

    while i < n - 1:
        if nums[i - 1] < nums[i] < nums[i + 1]:
            return i
        i += 1

    if nums[0] < nums[-1]:
        return n - 1
    else:
        return 0


def findPeakElement(nums: List[int]) -> int:
    """
    Time Complexity = O(logN) ; N = no. of elements in array
    Space Complexity = O(1)
    """
    n = len(nums)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if mid + 1 < n and nums[mid] < nums[mid + 1]:
            start = mid + 1
        elif mid - 1 > -1 and nums[mid] < nums[mid - 1]:
            end = mid - 1
        else:
            return mid
