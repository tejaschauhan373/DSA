# https://leetcode.com/problems/house-robber-ii/
# For naive and top down DP approach, refer house robber I
from typing import List


def find(nums):
    n = len(nums)

    # Corner case
    if n == 1:
        return max(0, nums[0])

    if n == 2:
        return max(0, max(nums[0], nums[1]))

    # Bottom Up Logic
    first = nums[0]
    second = max(nums[0], nums[1])

    for i in range(2, n):
        include = first + nums[i]
        exclude = second
        first = second
        second = max(include, exclude)

    return second

# Bottom Up
def rob(nums: List[int]) -> int:
    """
    Time Complexity = O(2N) ~= O(N)
    Space Complexity = O(2N) ~= O(N)
    ; N = length of nums
    """
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return max(0, max(nums[1], nums[0]))

    return max(find(nums[1:]), find(nums[:len(nums) - 1]))
