# https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1/?track=amazon-trees&batchId=192#
class Solution:

    def find_node(self, root, target):
        if root is None:
            return None

        if root.data == target:
            return root

        res_left = self.find_node(root.left, target)
        if res_left is not None:
            return res_left

        res_right = self.find_node(root.right, target)
        if res_right is not None:
            return res_right

        return None

    def find_dist_from_root(self, root, target):
        if root is None:
            return 0

        if root.data == target:
            return 1

        left = self.find_dist_from_root(root.left, target)
        if left != 0:
            return 1 + left

        right = self.find_dist_from_root(root.right, target)
        if right != 0:
            return 1 + right

        return 0

    def findDist(self, root, a, b):
        n1 = a
        n2 = b
        n1 = self.find_node(root, n1)
        n2 = self.find_node(root, n2)

        def add_parent(root, parent):
            if root:
                root.parent = parent
                add_parent(root.left, root)
                add_parent(root.right, root)

        n1_parents = {}
        add_parent(root, None)

        while n1:
            n1_parents[n1] = None
            n1 = n1.parent

        while n2 and n2 not in n1_parents:
            n2 = n2.parent

        a_len = self.find_dist_from_root(n2, a)
        b_len = self.find_dist_from_root(n2, b)
        return a_len + b_len - 2
