# https://leetcode.com/problems/subarray-product-less-than-k/
from typing import List


def num_sub_array_product_less_than_k(nums: List[int], k: int) -> int:
    """
    Time Complexity = O(N); N = len(nums)
    Space Complexity = O(1)
    """
    if k <= 1: return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1

    return ans
