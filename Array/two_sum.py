def find_pair_with_sum(nums: list, target: int):
    num_with_index = {}

    for i in range(len(nums)):
        if (target - nums[i]) in num_with_index:
            return [num_with_index[target - nums[i]], i]
        num_with_index[nums[i]] = i


print(find_pair_with_sum([2, 7, 11, 15], 9))
