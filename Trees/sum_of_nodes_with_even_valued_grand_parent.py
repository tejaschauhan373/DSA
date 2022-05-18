# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_sum(root, i):
    if root is None:
        return 0

    if i == 2:
        return root.val

    ans = 0
    ans += get_sum(root.left, i + 1)
    ans += get_sum(root.right, i + 1)
    return ans


def add_sum(root):
    if root is None:
        return 0
    ans = 0
    if root.val % 2 == 0:
        ans += get_sum(root, 0)

    ans += add_sum(root.left)
    ans += add_sum(root.right)
    return ans


def sum_even_grand_parent_brute(root: TreeNode) -> int:
    """
    Time Complexity = O(kN); k = 2
    Space Complexity = O(kN) # To store recursive call stack
    """
    return add_sum(root)


def sum_even_grand_parent_optimal_recursive(root: TreeNode) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N) # To store recursive call stack
    """

    def dfs(node: TreeNode, parent: Optional[TreeNode], grand_parent: Optional[TreeNode]):
        if not node:
            return
        nonlocal answer
        if parent and grand_parent and grand_parent.val % 2 == 0:
            answer += node.val
        dfs(node.left, node, parent)
        dfs(node.right, node, parent)

    answer = 0
    dfs(root, None, None)
    return answer


def sum_even_grand_parent_optimal_iterative(root: TreeNode) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N) # To store nodes of level at a time in stack
    """

    nodes_and_preds = [(root, None, None)]

    ans = 0
    while nodes_and_preds:
        node, parent, grand_parent = nodes_and_preds.pop()
        if parent and grand_parent and grand_parent.val % 2 == 0:
            ans += node.val

        if node.left:
            nodes_and_preds.append((node.left, node, parent))

        if node.right:
            nodes_and_preds.append((node.right, node, parent))

    return ans
