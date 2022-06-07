# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1/?track=amazon-trees&batchId=192
from collections import deque


def bottom_view(root):
    q = deque([(root, 0)])

    hash_map = {}
    while q:
        curr, cl = q.popleft()

        hash_map[cl] = curr.data

        if curr.left:
            temp = (curr.left, cl - 1)
            q.append(temp)

        if curr.right:
            temp = (curr.right, cl + 1)
            q.append(temp)

    return [hash_map[k] for k in sorted(hash_map.keys())]
