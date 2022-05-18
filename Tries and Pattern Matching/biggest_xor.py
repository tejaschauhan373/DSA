# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Node:
    def __init__(self):
        self.left = None  # consider as 0
        self.right = None  # consider as 1


class HybridTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, n):
        temp = self.root
        i = 31
        # bits of that number in trie
        while i >= 0:
            bit = (n >> i) & 1
            if bit == 0:
                if temp.left is None:
                    temp.left = Node()
                temp = temp.left  # go to that node
            else:
                if temp.right is None:
                    temp.right = Node()
                temp = temp.right
            i -= 1

    def max_xor_helper(self, value):
        current_ans = 0
        temp = self.root
        i = 31
        while i >= 0:
            bit = (value >> i) & 1
            if bit == 0:
                if temp.right is not None:
                    temp = temp.right
                    current_ans += (1 << i)
                else:
                    temp = temp.left
            else:
                if temp.left is not None:
                    temp = temp.left
                    current_ans += (1 << i)
                else:
                    temp = temp.right
            i -= 1
        return current_ans

    def max_xor(self, input, n):
        """
        Time Complexity = O(N)
        Space Complexity = O(N)
        """
        max_xor = 0
        for i in range(len(input)):
            value = input[i]
            self.insert(value)
            current_xor = self.max_xor_helper(value)
            max_xor = max(max_xor, current_xor)
        return max_xor


input = [3, 10, 5, 25, 9, 2]
t = HybridTrie()
print(t.max_xor(input, len(input)))
