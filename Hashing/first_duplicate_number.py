# https://leetcode.com/problems/find-the-duplicate-number
def find_duplicate(nums):
    """
    Time Complexity = O(N)
    Space Complexity  = O(N); N = number of elements in nums
    """

    res = {}

    for digit in nums:
        if digit in res:
            return digit
        res[digit] = None
