# https://leetcode.com/problems/power-of-three/
def is_power_of_three(n: int) -> bool:
    """
    Time Complexity = O(log(N))
    Space Complexity = O(1)
    """
    if n < 1:
        return False

    while n % 3 == 0:
        n = n // 3

    return n == 1
