# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
from Trees import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time Complexity = O(N) ; N = Number of Nodes in Tree
    Space Complexity = O(N); N = Number of Nodes in Tree
    """

    def add_parent(root, parent=None):
        if root:
            root.parent = parent  # Added extra property to each node, hence TC = O(N)
            add_parent(root.left, root)
            add_parent(root.right, root)

    p_ans = {}
    add_parent(root, None)  # Traverse all nodes in Tree, Hence TC= O(N)

    while p:  # Iterate till root node, hence TC = O(Hp)
        p_ans[p] = None
        p = p.parent

    temp = q
    while temp and temp not in p_ans:
        temp = temp.parent

    return temp
