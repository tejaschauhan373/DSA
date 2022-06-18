# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


# Brute Force : O(N*N); To find all sub array

# Optimal
def max_product(nums: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    n = len(nums)
    res = nums[0]
    l = 0
    r = 0
    for i in range(n):
        if l:
            l *= nums[i]
        else:
            l = 1 * nums[i]

        if r:
            r *= nums[n - i - 1]
        else:
            r = 1 * nums[n - i - 1]

        res = max(res, max(l, r))

    return res
