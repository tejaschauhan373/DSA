a = list(map(int, input().split(' ')))


def max_and_min(a, n):
    r = {'max': a[0], 'min': a[0]}
    if n == 1:
        return r
    else:
        if a[1] > a[0]:
            r['min'] = a[0]
            r['max'] = a[1]
        else:
            r['min'] = a[1]
            r['max'] = a[0]

        for i in range(2, n):
            if a[i] < r['min']:
                r['min'] = a[i]

            if a[i] > r['max']:
                r['max'] = a[i]

    return r


print(max_and_min(a, len(a)))
