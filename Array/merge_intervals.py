# https://leetcode.com/problems/merge-intervals

def merge(intervals):
    """
    Time Complexity = O(Nlog(N)) ; N = len(intervals)
    Space Complexity = O(1) ; We don't consider space complexity of output.
    """
    intervals.sort(key=lambda x: x[0])  # TC = time sort, O(Nlog(N))
    ans = []
    i = 1
    n = len(intervals)

    last = intervals[0]
    while i < n:
        if last[-1] >= intervals[i][0]:
            last[-1] = max(intervals[i][-1], last[-1])
        else:
            ans.append(last)
            last = intervals[i]
        i += 1

    ans.append(last)
    return ans


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [0, 4]]))
