from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
    :param nums: list of numbers
    :return: length of maximum consecutive numbers

    Time Complexity = O(nlogn) + O(n) ~= O(nlogn)
    Space Complexity = O(1)
    """
    if len(nums) == 0:
        return 0
    nums.sort()
    max_length = 1
    last = nums[0]
    temp_length = 1
    for i in range(1, len(nums)):
        if last == nums[i]:
            continue
        if last == nums[i] - 1:
            temp_length += 1
        else:
            temp_length = 1

        max_length = max(max_length, temp_length)
        last = nums[i]

    return max_length
