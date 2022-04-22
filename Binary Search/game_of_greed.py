def k_partitions(coins: list, friends: int, max_value: int) -> bool:
    current_friend = 0
    partitions = 0

    for i in range(len(coins)):

        if current_friend + coins[i] >= max_value:
            current_friend = 0
            partitions += 1
        else:
            current_friend += coins[i]

    return partitions >= friends


def find_max_coin_value(coins: list, friends: int) -> int:
    coins.sort()

    start = 0
    end = coins[-1]

    ans = -1

    while start <= end:
        mid = (start + end) // 2

        res = k_partitions(coins, friends, mid)

        if res:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans


coin = [10, 22, 40, 55]
print(find_max_coin_value(coin, 3))
