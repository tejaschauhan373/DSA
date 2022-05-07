# https://practice.geeksforgeeks.org/problems/search-a-node-in-bst

def search(self, node, x):
    """
    Time Complexity in worst case = O(H) ; H = height of Tree
    """
    if node is None:
        return False

    if node.data == x:
        return True

    if node.data > x:
        return self.search(node.left, x)
    else:
        return self.search(node.right, x)
