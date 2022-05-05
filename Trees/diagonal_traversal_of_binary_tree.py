def diagonal(root):
    def traversal(root, d, my_dict):

        if root is None:
            return

        try:
            my_dict[d].append(root.data)
        except:
            my_dict = [d]

        traversal(root.left, d + 1, my_dict)

        traversal(root.right, d, my_dict)

    my_dict = {}

    traversal(root, 0, my_dict)

    res = []
    for i in sorted(my_dict.keys()):
        res.extend(my_dict[i])

    return res
