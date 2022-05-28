# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
def recursive_check(n: int, ans):
    if n < 1:
        return False
    i = 0
    temp = 3 ** i
    while temp <= n:
        i += 1
        temp = 3 ** i
    if i - 1 not in ans:
        ans[i - 1] = n
    else:
        return False
    if 3 ** (i - 1) == n:
        return True
    else:
        return recursive_check(n - 3 ** (i - 1), ans)


def check_powers_of_three(n: int) -> bool:
    return recursive_check(n, {})
