import builtins
import http.client
from typing import List
from unittest.mock import patch
from TreeNode import TreeNode


class HDPair:
    def __init__(self):
        self.height = None
        self.diameter = None


def build_tree():
    d = int(input())

    if d == -1:
        return None

    n = TreeNode(d)
    n.left = build_tree()
    n.right = build_tree()

    return n


def level_order(root: TreeNode, new_level_separator: str = "", attr_name: str = "val") -> List[List[int]]:
    if root is None:
        return []

    top = [root]

    res = []

    while top:
        level = []
        bottom = []

        for i in top:
            if i.left:
                bottom.append(i.left)

            if i.right:
                bottom.append(i.right)

        for i in top:
            level.append(getattr(i, attr_name, i.val))

        level.append(new_level_separator)
        res.append(level)

        top = bottom

    return res


# helper function to calculate height of tree
def height(root: TreeNode):
    # base case
    if root is None:
        return 0

    # recursive case
    h1 = height(root.left)
    h2 = height(root.right)
    return 1 + max(h1, h2)


def diameter(root: TreeNode):
    """
    Time Complexity = O(N*N)
    """
    # base case
    if root is None:
        return 0

    # recursive case
    d1 = height(root.left) + height(root.right)
    d2 = diameter(root.left)
    d3 = diameter(root.right)
    return max(d1, d2, d3)


def opt_diameter(root: TreeNode):
    """
    Time Complexity = O(N)
    """
    p = HDPair()

    if root is None:
        p.height = p.diameter = 0
        return p

    left = opt_diameter(root.left)
    right = opt_diameter(root.right)

    p.height = max(left.height, right.height) + 1

    d1 = left.height + right.height
    d2 = left.diameter
    d3 = right.diameter

    p.diameter = max(d1, d2, d3)
    return p


def max_subset_sum(root: TreeNode):
    """
    Time Complexity = O(N)
    """
    ans = {}

    if root is None:
        return {"inc": 0, "exc": 0}

    left = max_subset_sum(root.left)
    right = max_subset_sum(root.right)

    ans["inc"] = root.val + left["exc"] + right["exc"]
    ans["exc"] = max(left["inc"], right["exc"]) + max(right["inc"], right["inc"])

    return ans


def get_tree(input: list = None):
    with patch('builtins.input') as input_mock:
        if input:
            input_mock.side_effect = input
        else:
            input_mock.side_effect = [
                "1", "2", "4", "-1", "-1", "5", "7", "-1", "-1", "-1", "3", "-1", "6", "-1", "-1"
            ]
        root = build_tree()
    return root


root = get_tree()
print(diameter(root))
print(opt_diameter(root).diameter)

print(max_subset_sum(root))

nodes = level_order(root)
for level in nodes:
    for j in level:
        print(j, end=" ")
    print()
