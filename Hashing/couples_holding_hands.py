# https://leetcode.com/problems/couples-holding-hands

def min_swaps_couples(row):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    pos = {val: i for i, val in enumerate(row)}

    i = 0
    swaps = 0
    while i < len(row):
        x = row[i]

        if x % 2 == 0:
            y = x + 1
        else:
            y = x - 1

        j = pos[y]

        if abs(j - i) > 1:
            row[i + 1], row[j] = row[j], row[i + 1]
            pos[row[j]] = j
            pos[y] = i + 1
            swaps += 1
        i += 1
    return swaps
