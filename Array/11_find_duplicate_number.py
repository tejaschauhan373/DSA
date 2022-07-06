def findDuplicate(nums) -> int:
    """
    Time Complexity = O(Nlog(N)) ; N = no. of elements in nums
    Space Complexity = O(1)
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
