# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
def count_primes(n: int) -> int:
    """
    Time Complexity = O(NLogLogN)
    Space Complexity = O(N)
    """
    if n <= 2:
        return 0

    prime_numbers = [0] * n
    for i in range(2, n):
        prime_numbers[i] = 1

    for i in range(2, n):
        if i * i >= n:
            break
        if not prime_numbers[i]:
            continue
        for j in range(i * i, n, i):
            prime_numbers[j] = 0
    return sum(prime_numbers)
