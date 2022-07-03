# https://leetcode.com/problems/permutations/
# https://leetcode.com/problems/permutations/discuss/2228668/simple-iterative-recursive-approach-in-python-with-visualization-of-recursive-tree
from typing import List


def permute_recursive(nums: List[int]) -> List[List[int]]:
    ans = []

    def permutation(temp_num: list, index: int, n: int):
        nonlocal ans
        if index == n - 1:
            ans.append(temp_num)

        for j in range(index, n):
            new_arr = list(temp_num)
            new_arr[index], new_arr[j] = new_arr[j], new_arr[index]
            permutation(new_arr, index + 1, n)

    permutation(nums, 0, len(nums))
    return ans


def permute_iterative(nums: List[int]) -> List[List[int]]:
    i = 0
    n = len(nums)
    level = [nums]

    while i < n - 1:
        size = len(level)
        for index in range(size):
            curr = level[index]
            for j in range(i + 1, n):
                new_nums = list(curr)
                new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
                level.append(new_nums)
        i += 1
    return level


print(permute_recursive([1, 2, 3]))
