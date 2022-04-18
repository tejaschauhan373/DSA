# https://practice.geeksforgeeks.org/problems/flip-bits0240/1/

def max_ones_brute(a: list, n: int):
    """
    Time Complexity = O(N*N)
    Space Complexity = O(1)
    """
    ori_one_c = 0
    max_diff = 0
    for i in range(n):

        if a[i] == 1:
            ori_one_c += 1

        one_c = 0
        zero_c = 0

        for j in range(i, n):
            if a[j] == 0:
                zero_c += 1
            else:
                one_c += 1

            max_diff = max(max_diff, zero_c - one_c)

    return ori_one_c + max_diff


def max_ones_optimal(a: list, n: int):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    ori_one_c = 0
    max_sum = 0
    temp_sum = 0
    for i in range(n):
        if a[i] == 1:
            ori_one_c += 1  
        if a[i] == 1:
            temp_sum -= 1
        else:
            temp_sum += 1

        if temp_sum < 0:
            temp_sum = 0

        max_sum = max(temp_sum, max_sum)

    return max_sum + ori_one_c


print(max_ones_brute([1, 0, 1, 0, 1, 0, 0, 1, 1], 5))
