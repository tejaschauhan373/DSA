# Definition for a binary tree node.

from typing import List
from TreeNode import TreeNode
from build_tree_boilerplate_code import get_tree


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


root = get_tree()
nodes = level_order(root)
for level in nodes:
    for j in level:
        print(j, end=" ")
    print()
