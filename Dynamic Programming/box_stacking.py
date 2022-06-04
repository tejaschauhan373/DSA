def find_box_stacking(arr: list):
    """
    Time Complexity ~= O(N^2))
    Space Complexity = O(N)
    """
    # Sorting
    arr.sort(key=lambda x: x[-1])  # TC = O(NlogN)
    n = len(arr)  # TC = O(1)

    # DP array
    dp_h = [0] * n  # TC = O(N)

    for i in range(n):
        curr_box = arr[i]
        curr_stack = curr_box[-1]  # height of ith box
        # Check for all boxes whose index is less than i
        for j in range(i + 1):
            temp_box = arr[j]
            if temp_box[0] < curr_box[0] and temp_box[1] < curr_box[1] and temp_box[2] < curr_box[2]:
                curr_stack = max(curr_stack, curr_box[-1] + dp_h[j])
        dp_h[i] = curr_stack

    """
    Time Complexity of Above For loop:
    How many times loop will iterate?

    loop count:

    1 -> 0 to 1 = [0, 1); i = 0, j = 0
    2 -> 0 to 2 = [0, 2); i = 1, j = 0, 1
    3 -> 0 to 3 = [0, 3); i = 2, j = 0, 1, 2
    4 -> 0 to 4 = [0, 4); i = 3, j = 0, 1, 2, 3
    5 -> 0 to 5 = [0, 5); i = 4, j = 0, 1, 2, 3, 4
    ...
    n -> 0 to n = [0, n); i = n - 1, j = 0, 1, ..., n - 1

    so sequence is [1, 2, 3, 4, ..., n]
    So, count of all for loop occurrence is total sum of above sequence

    here sequence is increased by 1 value with each element
    so, difference between any two elements : d = 1
    first element : a = 1
    total elements = n
    Formula to find the sum of series 
    = (n/2)([2a +(n - 1) d])
    = (n/2)[2(1) + (n - 1)(1)] ; a = 1, d = 1
    = (n/2)(2 + n - 1)
    = (n/2)(n + 1)
    = (n^2 + n)/2
    = O(n^2/2) + O(n/2)
    = O(N^2*k) + O(nk) ; let's assume k = 1/2 (constant)
    ~= O(N^2)                                 

    So, TC ~= O(N^2)
    """

    return max(dp_h)  # O(N)


if __name__ == "__main__":
    array = [
        (2, 2, 1),
        (2, 1, 2),
        (3, 2, 3),
        (2, 3, 4),
        (4, 4, 5),
        (2, 2, 8)
    ]
    print(find_box_stacking(array))
