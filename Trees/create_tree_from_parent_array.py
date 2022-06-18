class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def create_tree(parent):
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    ; N = len(parent)
    """
    hash_map = {}
    for i, v in enumerate(parent):
        if v not in hash_map:
            hash_map[v] = Node(v)
        hash_map[i] = Node(i)
        if v > i:
            hash_map[v].left = hash_map[i]
        else:
            hash_map[v].right = hash_map[i]

    return hash_map[-1].right


if __name__ == "__main__":
    N = 7
    parent = [-1, 0, 0, 1, 1, 3, 5]
    print(create_tree(parent))
