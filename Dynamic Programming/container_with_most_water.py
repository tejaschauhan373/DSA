# https://leetcode.com/problems/container-with-most-water/
from typing import List


def max_area(height: List[int]) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    i, j = 0, len(height) - 1

    res = 0
    while i < j:
        width = j - i
        min_height = min(height[i], height[j])
        area = width * min_height
        res = max(res, area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res
