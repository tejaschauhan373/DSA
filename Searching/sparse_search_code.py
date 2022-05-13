def find_word(arr, left, right, find):
    """
    Time Complexity in worst case = O(N)
    Time Complexity in Average case = O(LogN)
    Space Complexity = O(1)
    """
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == "":
        i = mid - 1
        j = mid + 1
        while arr[j] == "" and arr[i] == "" and j <= right and i >= left:
            j += 1
            i -= 1
        if arr[j] != "":
            mid = j
        else:
            mid = i

    if arr[mid] == find:
        return mid
    elif arr[mid] < find:
        return find_word(arr, mid + 1, right, find)
    else:
        return find_word(arr, left, mid - 1, find)


a = ["ai", "", "", "bat", "", "", "car", "car", "", "", "dog", "e"]
print(a[find_word(a, 0, len(a) - 1, "dog")])
