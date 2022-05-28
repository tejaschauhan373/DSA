# Without memoization
def fibonacci(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# With memoization
def fib(N):
    """
    :type N: int
    :rtype: int
    """
    cache = {}

    def recur_fib(N):
        if N in cache:
            return cache[N]

        if N < 2:
            result = N
        else:
            result = recur_fib(N - 1) + recur_fib(N - 2)

        # put result in cache for later reference.
        cache[N] = result
        return result

    return recur_fib(N)
