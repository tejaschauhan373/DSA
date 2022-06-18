# https://leetcode.com/problems/delete-and-earn/

from collections import defaultdict
from functools import lru_cache
from typing import List


# Recursive + Brute
def delete_and_earn_recursive(nums: List[int]) -> int:
    points = defaultdict(int)
    max_number = 0
    for num in nums:
        points[num] += num
        max_number = max(max_number, num)

    def find_max(number: int):
        if number == 0:
            return 0

        if number == 1:
            return points[1]

        return max(find_max(number - 1), find_max(number - 2) + points[number])

    return find_max(max_number)


# Recursive + LRU cache
def delete_and_earn_top_down(nums: List[int]) -> int:
    points = defaultdict(int)
    max_number = 0
    for num in nums:
        points[num] += num
        max_number = max(max_number, num)

    @lru_cache()
    def find_max(number: int):
        if number == 0:
            return 0

        if number == 1:
            return points[1]

        return max(find_max(number - 1), find_max(number - 2) + points[number])

    return find_max(max_number)


# Bottom Up DP
def delete_and_earn_bottom_up(nums: List[int]) -> int:
    points = defaultdict(int)
    max_number = 0
    for num in nums:
        points[num] += num
        max_number = max(max_number, num)

    # Base case
    two_back = 0
    one_back = points.get(1, 0)

    for num in range(2, max_number + 1):
        two_back, one_back = one_back, max(one_back, two_back + points.get(num, 0))

    return one_back
