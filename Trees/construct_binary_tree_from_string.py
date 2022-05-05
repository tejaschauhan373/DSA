class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def preOrder(node):
    if (node == None):
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


def findIndex(Str, si, ei):
    if (si > ei):
        return -1

    s = []
    for i in range(si, ei + 1):

        if (Str[i] == '('):
            s.append(Str[i])

        elif (Str[i] == ')'):
            if (s[-1] == '('):
                s.pop(-1)

                if len(s) == 0:
                    return i
    return -1


def treeFromString(Str, si, ei):
    # Base case
    if (si > ei):
        return None

    # new root
    root = newNode(ord(Str[si]) - ord('0'))
    index = -1

    # if next char is '(' find the
    # index of its complement ')'
    if (si + 1 <= ei and Str[si + 1] == '('):
        index = findIndex(Str, si + 1, ei)

    # if index found
    if (index != -1):
        # call for left subtree
        root.left = treeFromString(Str, si + 2,
                                   index - 1)

        # call for right subtree
        root.right = treeFromString(Str, index + 2,
                                    ei - 1)
    return root


# Driver Code
if __name__ == '__main__':
    Str = "4(2(3)(1))(6(5))"
    root = treeFromString(Str, 0, len(Str) - 1)
    preOrder(root)
