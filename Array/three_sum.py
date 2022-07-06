# https://leetcode.com/problems/3sum/
from typing import List, Tuple


def three_sum(nums: List[int]) -> List[Tuple[int, int, int]]:
    """
    :param nums: list of numbers
    :return: list of unique triplets with given sum

    Implemented using two sum (two pointers)
    Time Complexity = O(n^2)
    Space Complexity = O(1) ; We don't consider space complexity of output.
    """
    n = len(nums)
    if n < 3:
        return []

    nums.sort()
    target = 0
    answer = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        rem = target - nums[i]
        start, end = i + 1, len(nums) - 1

        while start < end:
            curr_sum = nums[start] + nums[end]

            if curr_sum < rem:
                start += 1
            elif curr_sum > rem:
                end -= 1
            else:
                answer.append((nums[i], nums[start], nums[end]))
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1
                start += 1
                end -= 1
    return answer
