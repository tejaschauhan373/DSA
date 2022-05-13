# https://leetcode.com/problems/first-missing-positive/

def first_missing_positive(nums):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    res_d = {}

    for num in nums:
        res_d[num] = None

    i = 1

    while i < len(nums) + 1:
        if i not in res_d:
            return i
        i += 1

    return i
