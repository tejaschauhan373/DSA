# https://leetcode.com/problems/maximum-score-of-spliced-array/
from typing import List


def maximumsSplicedArray(nums1: List[int], nums2: List[int]) -> int:
    """
    Time Complexity = O(N) ; N = len(nums1)
    Space Complexity = O(N) ; N = len(nums1)
    """
    sum_nums1 = 0
    sum_nums2 = 0
    diff_nums1 = []
    diff_nums2 = []

    for x, y in zip(nums1, nums2):
        sum_nums1 += x
        sum_nums2 += y
        diff_nums1.append(y - x)
        diff_nums2.append(x - y)

    def find_max_sum_array(nums):
        # TC = O(N) ; N = len(nums)
        # SC = O(1)
        # Kadane's algorithm
        total_max = nums[0]
        temp_max = nums[0]

        for num in nums[1:]:
            temp_max = max(num, temp_max + num)
            total_max = max(total_max, temp_max)

        return total_max

    sub_arr_nums1 = find_max_sum_array(diff_nums1)
    sub_arr_nums2 = find_max_sum_array(diff_nums2)

    return max(sum_nums1 + sub_arr_nums1, sum_nums2 + sub_arr_nums2)
