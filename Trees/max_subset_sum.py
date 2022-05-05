from TreeNode import TreeNode
from build_tree_boilerplate_code import get_tree


def max_subset_sum(root: TreeNode):
    ans = {}

    if root is None:
        return {"inc": 0, "exc": 0}

    left = max_subset_sum(root.left)
    right = max_subset_sum(root.right)

    ans["inc"] = root.val + left["exc"] + right["exc"]
    ans["exc"] = max(left["inc"], right["exc"]) + max(right["inc"], right["inc"])

    return ans


root = get_tree()
print(max_subset_sum(root))
