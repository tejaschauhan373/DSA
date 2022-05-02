from collections import deque


def first_non_repeating(nums: str):
    res = ""
    my_d = deque()
    fre_c = {}

    for char in nums:
        if char not in fre_c:
            fre_c[char] = 1
        else:
            fre_c[char] += 1
        my_d.append(char)

        while my_d and fre_c[my_d[0]] > 1:
            my_d.popleft()

        if my_d:
            res += my_d[0]
        else:
            res += '#'

    return res


print(first_non_repeating("aabc"))
