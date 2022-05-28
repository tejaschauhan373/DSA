# https://www.udemy.com/course/cpp-data-structures-algorithms-levelup-prateek-narang/learn/lecture/23546720#overview
# Not for interview, but for good practice
# (8-way DFS + Trie guided search + Backtracking)
class Node:

    def __init__(self, s):
        self.s = s
        self.is_terminal = False
        self.word = ""
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node(None)

    def add_word(self, word):
        temp = self.root

        for char in word:
            if char not in temp.children:
                n = Node(char)
                temp.children[char] = n
            temp = temp.children[char]

        # last node
        temp.is_terminal = True
        temp.word = word


def dfs(board: list, node: Node, i: int, j: int, visited_space: list, ans: set):
    # base case
    char = board[i][j]
    if char not in node.children:
        return

    # Otherwise trie contains this node
    visited_space[i][j] = True
    node = node.children[char]

    # If it is a terminal node in the trie
    if node.is_terminal:
        ans.add(node.word)

    # Explore the neighbours
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for k in range(8):
        ni = i + dx[k]
        nj = j + dy[k]

        # if it is in bounds and is not in visited
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not visited_space[ni][nj]:
            dfs(board, node, ni, nj, visited_space, output)

    # last step (backtracking)
    visited_space[i][j] = False


words = [
    "SNAKE",
    "FOR",
    "QUEZ",
    "SNACK",
    "SNACKS",
    "GO",
    "TUNES",
    "CAT"
]

boggle = [
    ["S", "E", "R", "T"],
    ["U", "N", "K", "S"],
    ["T", "C", "A", "T"]
]

M = len(boggle)  # number of rows
N = len(boggle[0])  # number of columns

# Main Algorithm (8-way DFS + Trie guided search)

# 1. Trie
t = Trie()
for word in words:
    t.add_word(word)

# 2. Take a set to store words that are found in dfs search
output = set()

# 3. Step (8 - DFS search from every cell)
visited = [[False for _ in range(N)] for _ in range(M)]

for i in range(M):
    for j in range(N):
        dfs(boggle, t.root, i, j, visited, output)
        # reset the visited array after every cell (while backtracking)

# 4. print the output, word present in boggle
for word in output:
    print(word)
