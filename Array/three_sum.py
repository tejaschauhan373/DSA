from typing import List, Tuple


def three_sum(nums: List[int]) -> List[Tuple[int, int, int]]:
    """
    :param nums: list of numbers
    :return: list of unique triplets with given sum

    Implemented using two sum (two pointers)
    Time Complexity = O(n^2)
    Space Complexity = O(n/3)
    """
    answer = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                answer.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return answer
