class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]

root = Node(arr[0])
for i in range(1, len(arr)):
    x = arr[i]
    root = insert(root, x)

print(root.left.left.val)
