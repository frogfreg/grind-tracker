def invert(root):
    if not root:
        return

    dummy = root.left
    root.left = invert(root.right)
    root.right = invert(dummy)

    return root
