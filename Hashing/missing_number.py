# https://leetcode.com/problems/missing-number/

def missing_number_optimal_brute(nums):
    """
    Time Complexity = O(N*N)
    Space Complexity = O(1)
    """
    i = 0
    while i < len(nums):
        if i not in nums:
            return i
        i += 1
    return i


def missing_number_optimal_one(nums):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    nums_d = {}

    for num in nums:
        nums_d[num] = None

    i = 0

    while i < len(nums):
        if i not in nums:
            return i
        i += 1
    return i


def missing_number_optimal_two(nums):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    xor = 0
    i = 0
    while i < len(nums):
        xor = xor ^ i ^ nums[i]
        i += 1
    return xor ^ i


def missing_number_optimal_two_another(nums):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    result = len(nums)
    for i in range(len(nums)):
        result += i - nums[i]
    return result
