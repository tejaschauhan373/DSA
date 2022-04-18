# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

def find_unsorted_sub_array(nums: list) -> int:
    """
    Time Complexity = O(NlogN)
    Space Complexity = O(N)
    """

    new_a = sorted(nums)

    i = 0
    while i < len(nums) and nums[i] == new_a[i]:
        i += 1

    j = len(nums) - 1

    if i < j:
        while j >= 0 and nums[j] == new_a[j]:
            j -= 1

    return j - i + 1


def find_unsorted_sub_array_optimal(nums: list) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    i = 0

    while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
        i += 1

    if i == len(nums) - 1:
        return 0

    j = len(nums) - 1

    while j > 0 and nums[j - 1] <= nums[j]:
        j -= 1

    my_max = float("-inf")
    my_min = float("+inf")

    for k in range(i, j + 1):
        my_max = max(my_max, nums[k])
        my_min = min(my_min, nums[k])

    kj = len(nums) - 1

    while kj > j:
        if my_max > nums[kj]:
            j = kj
            break
        kj -= 1

    ki = 0

    while ki < i:
        if my_min < nums[ki]:
            i = ki
            break
        ki += 1

    return j - i + 1


print(find_unsorted_sub_array_optimal([2, 6, 4, 8, 10, 9, 15]))
