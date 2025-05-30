def lca(root, p, q):
    low = min(p.val, q.val)
    high = max(p.val, q.val)

    while True:
        if root.val > high:
            root = root.left
            continue

        if root.val < low:
            root = root.right
            continue

        return root
