# https://practice.geeksforgeeks.org/problems/check-if-subtree/1/?track=amazon-trees&batchId=192#

class Solution:

    def find_node(self, root, target):
        if root is None:
            return

        if root.data == target.data:
            self.ans.append(root)

        self.find_node(root.left, target)
        self.find_node(root.right, target)

    def travel_parallel(self, T, S):
        if T is None and S is None:
            return True

        if T is None or S is None:
            return False

        if T.data != S.data:
            return False

        left = self.travel_parallel(T.left, S.left)
        right = self.travel_parallel(T.right, S.right)
        return left and right

    def isSubTree(self, T, S):
        self.ans = []
        self.find_node(T, S)
        res = False
        for i in self.ans:
            res = self.travel_parallel(i, S)
            if res:
                return True

        return res
