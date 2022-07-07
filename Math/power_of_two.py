# https://leetcode.com/problems/power-of-two
from math import log2, floor


def is_power_of_two_recursive(n: int):
    """
    Time Complexity = O(log(n))
    Space Complexity = O(log(n))
    """
    if n == 0:
        return False
    return n == 1 or (n % 2 == 0 and is_power_of_two_recursive(n // 2))


def is_power_of_two_iterative(n: int):
    """
    Time Complexity = O(log(n))
    Space Complexity = O(1)
    """
    if n == 0:
        return False

    while n % 2 == 0:
        n = n // 2

    return n == 1


def is_power_of_two_using_log(n: int):
    """
    Time Complexity = O(log(n))
    Space Complexity = O(1)
    """
    return n > 0 and log2(n) == floor(log2(n))


def is_power_of_two_using_binary(n: int):
    """
    Time Complexity = O(log(n))
    Space Complexity = O(1)
    """
    return n > 0 and bin(n).count('1') == 1


def is_power_of_two_using_bit(n: int):
    """
    Time Complexity = O(1)
    Space Complexity = O(1)
    """
    return n > 0 and n & (n - 1) == 0


def is_power_of_two_using_math(n: int):
    """
    Time Complexity = O(1)
    Space Complexity = O(1)
    """
    return n > 0 and (1 << 31) % n == 0


def is_power_of_two_using_pre_compute(n: int):
    """
    Time Complexity = O(1)
    Space Complexity = O(1)
    """
    power_of_2 = set(2 ** i for i in range(32))
    return n in power_of_2
