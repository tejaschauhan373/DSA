# https://leetcode.com/problems/house-robber

# Bottom Up Approach + DP + Iterative
def max_subset_sum_no_adjacent(array: list):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    n = len(array)
    dp = [0] * n

    # Corner case
    if n == 1:
        return max(0, array[0])

    if n == 2:
        return max(0, max(array[0], array[1]))

    # Bottom Up Logic
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, n):
        include = dp[i - 2] + array[i]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)

    return dp[n - 1]


# Bottom Up Approach + Fine Tuning + Iterative
def max_subset_sum_no_adjacent_optimized(array: list):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    n = len(array)

    # Corner case
    if n == 1:
        return max(0, array[0])

    if n == 2:
        return max(0, max(array[0], array[1]))

    # Bottom Up Logic
    first = array[0]
    second = max(array[0], array[1])

    for i in range(2, n):
        include = first + array[i]
        exclude = second
        first = second
        second = max(include, exclude)

    return second


if __name__ == "__main__":
    arr = [6, 10, 12, 7, 9, 14]
    print(max_subset_sum_no_adjacent(arr))
    print(max_subset_sum_no_adjacent_optimized(arr))
