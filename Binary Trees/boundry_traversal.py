from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def printBoundaryView(self, root):
        if root is None:
            return []

        all_data = [root.data]

        def left_boundry_tree(root):
            if root is None:
                return

            if root.left:
                all_data.append(root.data)
                left_boundry_tree(root.left)
            elif root.right:
                all_data.append(root.data)
                left_boundry_tree(root.right)

        right = []

        def right_boundry_tree(root):

            if root is None:
                return

            if root.right:
                right.insert(0, root.data)
                right_boundry_tree(root.right)
            elif root.left:
                right.insert(0, root.data)
                right_boundry_tree(root.left)

        def leave_node(root):
            if root and root.left is None and root.right is None:
                all_data.append(root.data)

            if root.left is not None:
                leave_node(root.left)

            if root.right is not None:
                leave_node(root.right)

        if root.left is not None:
            left_boundry_tree(root.left)

        leave_node(root)

        if root.right is not None:
            right_boundry_tree(root.right)

        return all_data + right


def buildTree(s):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))

    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)

    size = size + 1

    i = 1

    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size -= 1

        currVal = ip[i]

        if (currVal != "N"):
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1

        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1

        i += 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print(i, end=" ")
