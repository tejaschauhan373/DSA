# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:

    def __init__(self, d):
        self.data = d
        self.child = {}
        self.is_terminal = False


class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def add_word(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.child:
                n = Node(char)
                temp.child[char] = n
            temp = temp.child[char]
        temp.is_terminal = True

    def in_depth(self, word: str, temp):
        for i in range(len(word)):
            char = word[i]
            if char == ".":
                for cha in temp.child:
                    res = self.in_depth(cha + word[i + 1:], temp)
                    if res:
                        return True
            if char not in temp.child:
                return False
            temp = temp.child[char]
        return temp.is_terminal

    def search(self, word: str) -> bool:
        temp = self.root

        for i in range(len(word)):
            char = word[i]
            if char == ".":
                for cha in temp.child:
                    res = self.in_depth(cha + word[i + 1:], temp)
                    if res:
                        return True
            if char not in temp.child:
                return False
            temp = temp.child[char]
        return temp.is_terminal
