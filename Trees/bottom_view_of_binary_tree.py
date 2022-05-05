def bottomView(root):
    glo_d = {}

    que = [root]
    root.hd = 0
    while que:
        root = que[0]
        hd = root.hd

        glo_d[hd] = root.data

        if (root.left):
            root.left.hd = hd - 1
            que.append(root.left)

        if (root.right):
            root.right.hd = hd + 1
            que.append(root.right)

        que.pop(0)

    return [glo_d[i] for i in sorted(glo_d.keys())]
