def merge(intervals):
    a = []
    intervals.sort(key=lambda x: x[0])
    last = intervals[0]
    i = 1
    if len(intervals) == 1:
        return intervals

    while i < len(intervals):
        if last[-1] >= intervals[i][0]:
            last = [min(last[0], intervals[i][0]), max(last[-1], intervals[i][-1])]
            i += 1
        else:
            a.append(last)
            last = intervals[i]
            i += 1

    if not a or last != a[-1]:
        a.append(last)

    return a


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [0, 4]]))
