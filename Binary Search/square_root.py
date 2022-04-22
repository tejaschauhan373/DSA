# Find the square root of code up with given precision
# https://leetcode.com/problems/sqrtx

def find_square_root(number: int, precision: int) -> float:
    start = 0
    end = number
    ans = float("+inf")

    # Binary Search (Search Space 0....N)
    while start <= end:
        mid = (start + end) // 2

        if mid * mid == number:
            return mid
        elif mid * mid < number:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    # Linear Search (for floating part)
    inc = 0.1

    for i in range(precision):

        # do linear search
        while ans * ans <= number:
            ans += inc

        # Take one step back
        ans -= inc
        inc = inc / 10

    return ans


print(find_square_root(10, 3))
