# https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s
def max_len_brute(arr):
    """
    Time Complexity = O(N*N)
    Space Complexity = O(1)
    """
    max_length = 0
    for i in range(len(arr)):
        count = 0
        length = 0
        while i < len(arr):
            char = arr[i]
            if char == 0:
                count -= 1
            elif char == 1:
                count += 1
            length += 1
            if count == 0:
                max_length = max(length, max_length)
            i += 1
    return max_length


def max_len_optimal(arr):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    sum_dict = {0: -1}
    max_len = 0
    count = 0

    for i, num in enumerate(arr):
        count += 1 if arr[i] == 1 else -1
        if count in sum_dict:
            max_len = max(max_len, i - sum_dict[count])
        else:
            sum_dict[count] = i
    return max_len
