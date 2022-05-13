class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_rectangles(arr: list) -> int:
    # 1. Insert all Points in the Set

    all_point_dict = {p1: None for p1 in arr}
    ans = 0
    # 2. Logic Brute Force Two Points + LookUp for other Two
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            p1 = arr[i]
            p2 = arr[j]

            # small check that we want to make
            if p2.x == p1.x and p2.y == p1.y:
                continue

            # P3, P4
            p3 = Point(p1.x, p2.y)
            p4 = Point(p2.x, p1.y)

            # LookUp
            if p3 in all_point_dict and p4 in all_point_dict:
                ans += 1
    return ans // 2


all_points = [
    Point(4, 1),
    Point(4, 0),
    Point(0, 0),
    Point(0, 1),
    Point(1, 1),
    Point(1, 0),
    Point(2, 0),
    Point(2, 1),
]
print(get_rectangles(all_points))
