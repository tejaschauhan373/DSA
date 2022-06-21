# Find the maximum distance between birds
# https://leetcode.com/problems/magnetic-force-between-two-balls/

def can_place_birds(birds: int, nests: int, positions: list, distance: int) -> bool:
    placed = 1
    last_location = positions[0]

    for i in range(1, nests):
        current_location = positions[i]

        if current_location - last_location >= distance:
            placed += 1
            last_location = current_location

            if placed == birds:
                return True

    return False


def find_maximum_distance_between_birds(birds: int, nests: int, positions: list) -> int:
    """
    Time Complexity = O(Nlog(N)); N = len(positions)
    Space Complexity = O(1)
    """
    positions.sort()
    start = 0
    end = positions[-1] - positions[0]
    ans = -1

    while start <= end:

        mid = (start + end) // 2

        result = can_place_birds(birds, nests, positions, mid)

        if result:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans


a = [1, 2, 4, 8, 9]
b = 4
print(find_maximum_distance_between_birds(b, len(a), a))
