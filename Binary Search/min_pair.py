def lower_bound(arr: list, k: int) -> int:
    s = 0
    e = len(arr) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] >= k:
            ans = mid
            e = mid - 1
        elif arr[mid] > k:
            e = mid - 1
        else:
            s = mid + 1

    return ans


def find_min_pair(first_list: list, second_list: list) -> tuple:
    first_list.sort()
    p1 = first_list[0]
    p2 = second_list[0]
    diff = float("+inf")

    for x in second_list:

        lb_idx = lower_bound(first_list, x)

        if lb_idx != -1 and abs(x - first_list[lb_idx]) < diff:
            diff = abs(x - first_list[lb_idx])
            p2 = x
            p1 = first_list[lb_idx]

        if lb_idx == -1 and abs(first_list[-1] - x < diff):
            diff = abs(first_list[-1] - x)
            p1 = x
            p2 = first_list[-1]

    return p1, p2


a1 = [-1, 5, 10, 20, 3]
a2 = [26, 134, 135, 15, 17]

print(find_min_pair(a1, a2))
