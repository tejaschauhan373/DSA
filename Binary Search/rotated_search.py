# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Find the element in given sorted rotated array

def modified_binary_search(nums: list, target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[start] <= nums[mid]:  # check if start to mid is sorted in ascending order or not

            if nums[mid] > target >= nums[start]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


a = [1, 0, 1, 1, 1]
print(modified_binary_search(a, 0))
