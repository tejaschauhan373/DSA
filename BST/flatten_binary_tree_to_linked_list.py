# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from Trees import TreeNode
from typing import Optional


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def tree_to_linked_list(root):
    """
    Time Complexity = O(N)
    Space Complexity = O(H) ; H = height of tree
    """
    l = LinkedList()
    if root is None:
        l.head = l.tail = None
        return l

    if root.left is None and root.right is None:
        l.head = l.tail = root
        root.left = None
        return l
    elif root.left and root.right is None:
        leftLL = tree_to_linked_list(root.left)
        root.right = leftLL.head
        l.head = root
        l.tail = leftLL.tail
    elif root.left is None and root.right:
        rightLL = tree_to_linked_list(root.right)
        root.right = rightLL.head
        l.head = root
        l.tail = rightLL.tail
    else:
        leftLL = tree_to_linked_list(root.left)
        rightLL = tree_to_linked_list(root.right)
        root.right = leftLL.head
        leftLL.tail.right = rightLL.head
        l.head = root
        l.tail = rightLL.tail

    root.left = None
    return l


def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    tree_to_linked_list(root)
