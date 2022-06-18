# https://leetcode.com/problems/water-and-jug-problem/


from collections import deque


def can_measure_water_bfs(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    z = targetCapacity
    x = jug1Capacity
    y = jug2Capacity
    if x > y:
        x, y = y, x

    if z > x + y:
        return False

    # set the initial state with empty jars
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    while len(queue) > 0:
        a, b = queue.popleft()
        if a + b == z:
            return True
        states = set()

        states.add((x, b))  # fill jar x
        states.add((a, y))  # fill jar y
        states.add((0, b))  # empty jar x
        states.add((a, 0))  # empty jar y
        # pour jar y to x
        states.add((min(x, b + a), 0 if b < x - a else b - (x - a)))
        # pour jar x to y
        states.add((0 if a + b < y else a - (y - b), min(b + a, y)))

        for state in states:
            if state in visited:
                continue
            queue.append(state)
            visited.add(state)

    return False


def can_measure_water(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    if targetCapacity > jug1Capacity + jug2Capacity:
        return False

    if targetCapacity == jug1Capacity:
        return True
    elif jug2Capacity == targetCapacity:
        return True
    elif jug1Capacity + jug2Capacity == targetCapacity:
        return True

    def gcd(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
