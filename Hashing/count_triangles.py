def count_triangles(points: list):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    freq_x = {}
    freq_y = {}

    # count the frequency by iterating over all the points
    for p in points:
        x = p[0]
        y = p[1]
        if x in freq_x:
            freq_x[x] += 1
        else:
            freq_x[x] = 1

        if y in freq_y:
            freq_y[y] += 1
        else:
            freq_y[y] = 1

    # count
    count = 0
    for p in points:
        x = p[0]
        y = p[1]

        fx = freq_x[x]
        fy = freq_y[y]

        count += (fx - 1) * (fy - 1)

    return count


points = [
    (1, 2),
    (2, 0),
    (2, 2),
    (2, 3),
    (4, 2)
]
print(count_triangles(points))
