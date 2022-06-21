def brute_force(numbers: list, target_sum: int) -> list:
    """
    :param numbers: list of numbers
    :param target_sum: sum of pair should be
    :return: list of pair with given sum

    Time complexity : O(n^2)
    Space complexity : O(1)
    """
    all_pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                all_pairs.append([numbers[i], numbers[j]])
    return all_pairs


def binary_search(numbers: list, low: int, high: int, find_num: int) -> int:
    """
    :param numbers: sorted list of numbers
    :param low: starting index of window
    :param high: ending index of window
    :param find_num: number to find in window
    :return: index of target number if present else return -1
    """
    if low <= high:
        mid = (high + low) // 2
        if numbers[mid] == find_num:
            return mid
        elif numbers[mid] > find_num:
            return binary_search(numbers, low, mid - 1, find_num)
        else:
            return binary_search(numbers, mid + 1, high, find_num)

    return -1


def moderate_bin_search(numbers: list, target_sum: int) -> list:
    """
    :param numbers: list of numbers
    :param target_sum: sum of pair should be
    :return: list of pair with given sum

    Time complexity = O(nlog(n))
    Space Complexity = O(1)
    """
    all_pairs = []
    numbers.sort()
    for i in range(len(numbers)):
        curr_num = numbers[i]
        find_num = target_sum - curr_num
        index = binary_search(numbers, 0, len(numbers) - 1, find_num)
        if index != - 1 and index != i:
            all_pairs.append([numbers[i], numbers[index]])
    return all_pairs


def optimize_map(numbers: list, target_sum: int) -> list:
    """
    :param numbers: list of numbers
    :param target_sum: sum of pair should be
    :return: list of pair with given sum

    Time complexity : O(n)
    Space complexity : O(n)
    """
    my_set = {}
    all_pairs = []
    for i in range(len(numbers)):
        my_set[numbers[i]] = numbers[i]
        find_num = target_sum - numbers[i]
        if find_num in my_set:
            all_pairs.append([numbers[i], find_num])

    return all_pairs


def two_pointer_approach(numbers: list, target_sum: int) -> list:
    """
    :param numbers: list of numbers
    :param target_sum: sum of pair should be
    :return: list of pair with given sum

    Time complexity : O(nlog(n)) with reduced space complexity or without using dictionary
    Space Complexity = O(1)
    """
    numbers.sort()  # TC = O(nlog(n))
    all_pairs = []
    i = 0
    j = len(numbers) - 1
    while i < j:  # TC = O(n)
        if numbers[i] + numbers[j] == target_sum:
            all_pairs.append([numbers[i], numbers[j]])
            i += 1
            j -= 1
        elif numbers[i] + numbers[j] < target_sum:
            i += 1
        else:
            j -= 1
    return all_pairs


print(brute_force([2, 7, 11, 15], 9))
print(moderate_bin_search([2, 7, 11, 15], 9))
print(optimize_map([2, 7, 11, 15], 9))
print(two_pointer_approach([2, 7, 11, 15, ], 9))
