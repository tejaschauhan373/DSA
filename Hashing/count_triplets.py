def count_triplets(arr: list, r: int) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """

    right = {}
    left = {}
    for x in arr:  # TC = O(N)
        if x in right:  # TC = O(1)
            right[x] += 1  # TC = O(1)
        else:
            right[x] = 1  # TC = O(1)
        left[x] = 0

    ans = 0

    for i in range(len(arr)):  # TC = O(N)
        right[arr[i]] -= 1

        if arr[i] % r == 0:
            b = arr[i]
            a = b / r
            c = b * r
            ans += left.get(a, 0) * right.get(c, 0)  # TC = O(1)

        left[arr[i]] += 1
    return ans


nums = [1, 16, 4, 16, 64, 16]
print(count_triplets(nums, 4))
