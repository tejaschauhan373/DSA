# https://leetcode.com/problems/implement-trie-prefix-tree

class Node:

    def __init__(self, d):
        self.data = d
        self.child = {}
        self.is_terminal = False


class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        temp = self.root

        for char in word:
            if char not in temp.child:
                n = Node(char)
                temp.child[char] = n
            temp = temp.child[char]
        temp.is_terminal = True

    def search(self, word) -> bool:
        temp = self.root

        for char in word:
            if char not in temp.child:
                return False
            temp = temp.child[char]

        return temp.is_terminal
