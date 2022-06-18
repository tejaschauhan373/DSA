# https://leetcode.com/problems/maximum-sum-circular-subarray/
# https://assets.leetcode.com/users/motorix/image_1538888300.png
from typing import List


def max_sub_array_sum_circular(nums: List[int]) -> int:
    """
    Time Complexity = O(N) ; N = length of nums
    Space Complexity = O(1)
    """
    total = 0
    max_sum = nums[0]
    curr_max = 0
    min_sum = nums[0]
    cur_min = 0

    for a in nums:
        curr_max = max(curr_max + a, a)
        max_sum = max(max_sum, curr_max)
        cur_min = min(cur_min + a, a)
        min_sum = min(min_sum, cur_min)
        total += a
    if max_sum > 0:
        return max(max_sum, total - min_sum)
    else:
        return max_sum
