# https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst
from collections import deque


def inorder_iterative(root):
    # create an empty stack
    stack = deque()
    ans = []
    # start from the root node (set current node to the root node)
    curr = root

    # if the current node is None and the stack is also empty, we are done
    while stack or curr:

        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            ans.append(curr)

            curr = curr.right
    return ans


def inorder_successor(root, x):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    """
    ans = inorder_iterative(root)  # get inorder traversal list

    start = 0
    end = len(ans) - 1
    got = False
    while start <= end:
        mid = (start + end) // 2

        if ans[mid].data == x.data:
            got = True
            break

        if ans[mid].data > x.data:
            end = mid - 1
        else:
            start = mid + 1

    if got and mid + 1 < len(ans):
        return ans[mid + 1]
    else:
        return None


def inorder_traversal(root, x):
    """
    Time Complexity = O(H); H = height of tree
    Space Complexity = O(1)
    """
    target = x

    temp = root
    succ = None
    while temp:

        if temp.data > target.data:
            succ = temp
            temp = temp.left
        elif temp.data < target.data:
            temp = temp.right
        else:
            break

    if temp.right:
        temp = temp.right
        while temp.left:
            temp = temp.left
        return temp

    return succ
