# https://leetcode.com/problems/4sum/

from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Time Complexity ~= O(N*N)
    Space Complexity = O(1)
    """
    nums.sort()
    n = len(nums)
    result = []

    i = 0

    while i < n:

        j = i + 1
        while j < n:

            target_2 = target - nums[i] - nums[j]

            front = j + 1
            back = n - 1

            while front < back:
                two_sum = nums[front] + nums[back]

                if two_sum < target_2:
                    front += 1
                elif two_sum > target_2:
                    back -= 1
                else:
                    quad = [nums[i], nums[j], nums[front], nums[back]]
                    result.append(quad)

                    while front < back and nums[front] == quad[2]:
                        front += 1

                    while front < back and nums[back] == quad[3]:
                        back -= 1

            while j + 1 < n and nums[j + 1] == nums[j]:
                j += 1

            j += 1

        while i + 1 < n and nums[i + 1] == nums[i]:
            i += 1

        i += 1
    return result
