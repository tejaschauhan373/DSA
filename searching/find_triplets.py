# Find the triplets with given sum in ascending order

# Naive  Approach is brute force
def find_triplets(numbers: list, target_sum: int):
    """
    :param numbers: list of numbers
    :param target_sum: sum of triplets
    :return: list of all triplets

    Time Complexity = O(n^3)
    """
    all_triplets = []
    numbers.sort()
    for i in range(len(numbers) - 2):
        for j in range(len(numbers) - 1):
            for k in range(len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == target_sum:
                    all_triplets.append([numbers[i], numbers[j], numbers[k]])
    return all_triplets


def optimize_map(numbers: list, target_sum: int) -> list:
    """
    :param numbers: list of numbers
    :param target_sum: sum of pair should be
    :return: list of pair with given sum

    Time complexity : O(n)
    """
    my_set = {}
    all_pairs = []
    for i in range(len(numbers)):
        my_set[numbers[i]] = numbers[i]
        find_num = target_sum - numbers[i]
        if find_num in my_set:
            all_pairs.append([numbers[i], find_num])

    return all_pairs


# Approach with medium time complexity : Solution: one for loop (N) *  two sum problem (N)
def find_triplets_using_two_sum(numbers: list, target_sum: int):
    """
    :param numbers: list of numbers
    :param target_sum: sum of triplets
    :return: list of all triplets

    Time Complexity = O(n^2)
    """
    all_triplets = []
    numbers.sort()
    for i in range(len(numbers)):
        curr_num = numbers[i]
        remain_sum = target_sum - curr_num
        pairs = optimize_map(numbers[i:], remain_sum)
        for two_sum_pair in pairs:
            two_sum_pair.append(curr_num)
            all_triplets.append(two_sum_pair)
    return all_triplets
