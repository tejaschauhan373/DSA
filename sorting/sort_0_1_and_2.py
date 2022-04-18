# https://leetcode.com/problems/sort-colors/

def sort_using_algo(arr: list):
    """
    Time Complexity = O(NlogN)
    Space Complexity = O(1)
    """
    arr.sort()


def sort_using_2n(nums: list):
    """
    Time Complexity = O(3N)
    Space Complexity = O(N)
    """
    temp = []

    i = 0
    while i < len(nums):
        if nums[i] == 0:
            temp.append(nums[i])
        i += 1

    i = 0
    while i < len(nums):
        if nums[i] == 1:
            temp.append(nums[i])
        i += 1

    i = 0
    while i < len(nums):
        if nums[i] == 2:
            temp.append(nums[i])
        i += 1

    i = 0
    while i < len(nums):
        nums[i] = temp[i]
        i += 1


def optimal(nums: list):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    mid = 0
    high = len(nums) - 1
    low = 0
    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
        else:
            mid += 1
