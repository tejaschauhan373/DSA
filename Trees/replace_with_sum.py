from TreeNode import TreeNode
from build_tree_boilerplate_code import get_tree
from level_order_traversal import level_order


def replace_with_sum(root: TreeNode):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val
    temp = root.val
    LS = replace_with_sum(root.left)
    RS = replace_with_sum(root.right)
    root.val = LS + RS
    return root.val + temp


root = get_tree()
root.data = replace_with_sum(root)
nodes = level_order(root)
for level in nodes:
    for j in level:
        print(j, end=" ")
    print()
