# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
from typing import List


def search(nums: List[int], target: int) -> bool:
    """
    Time Complexity = O(logN) in best case, O(N) in worst case (having all same element)
    Space Complexity = O(1)
    """
    if not nums:
        return False

    start = 0
    end = len(nums) - 1

    while start <= end:

        while start < end and nums[start] == nums[start + 1]:
            start += 1

        while start < end and nums[end] == nums[end - 1]:
            end -= 1

        mid = (start + end) // 2

        if nums[mid] == target:
            return True
        elif nums[start] <= nums[mid]:

            if nums[mid] > target >= nums[start]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return False
