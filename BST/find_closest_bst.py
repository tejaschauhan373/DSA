# https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst


def min_diff(root, K):
    """
    Iterative Approach
    Time Complexity = O(H) ; H = Height of Tree
    Space Complexity = O(1)
    """
    temp = root
    diff = float("+inf")

    while temp:
        current_diff = abs(temp.data - K)

        if current_diff < diff:
            diff = current_diff

        if current_diff == 0:
            diff = current_diff
            break

        if K > temp.data:
            temp = temp.right
        else:
            temp = temp.left
    return diff

    # code here


def find_min_diff(root, K):
    """
    Recursive Approach
    Time Complexity = O(H)
    Space Complexity = O(H) ; H = Height of Tree
    """
    if root is None:
        return float("+inf")

    current_diff = abs(root.data - K)

    if current_diff == 0:
        return 0

    if K > root.data:
        res = find_min_diff(root.right, K)
    else:
        res = find_min_diff(root.left, K)

    return min(current_diff, res)
