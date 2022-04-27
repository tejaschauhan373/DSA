# https://leetcode.com/problems/climbing-stairs/

def climb_stairs_recursive_brute(n: int) -> int:
    """
    Time Complexity = O(2^N)
    Space Complexity = O(N)
    """
    if n < 0:
        return 0

    if n == 0:
        return 1

    return climb_stairs_recursive_brute(n - 1) + climb_stairs_recursive_brute(n - 2)
