# https://leetcode.com/problems/sliding-window-median
from typing import List


def median_sliding_window_brute(nums: List[int], k: int) -> List[float]:
    """
    Time Complexity = O((N - k +1)*(KLogK))
    Space Complexity = O(K)
    """
    res = []
    for i in range(len(nums) - k + 1):
        temp = sorted(nums[i:i + k])
        if k == 0:
            res.append(temp[0])

        elif k % 2 == 0:
            res.append((temp[k // 2 - 1] + temp[k // 2]) / 2)
        else:
            res.append(temp[k // 2])
    return res
