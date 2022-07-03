# https://leetcode.com/problems/jump-game/
from typing import List


def can_jump(nums: List[int]) -> bool:
    n = len(nums)
    last = n - 1
    i = n - 2
    while i >= 0:
        if last <= i + nums[i]:
            last = i
        i -= 1

    if last <= 0:
        return True
    return False


if __name__ == "__main__":
    a = [2, 3, 1, 1, 4]
    print(can_jump(a))
