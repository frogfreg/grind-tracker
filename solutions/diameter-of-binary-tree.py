# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def diameterOfBinaryTree(root):
    if not root:
        return 0

    if (not root.left) and (not root.right):
        return 0

    return max(
        longestPathThroughNode(root),
        diameterOfBinaryTree(root.left),
        diameterOfBinaryTree(root.right),
    )


def longestPathThroughNode(root):
    if not root:
        return 0

    total = 0

    if root.left:
        total += 1 + height(root.left)

    if root.right:
        total += 1 + height(root.right)

    return total


def height(root):
    if not root:
        return 0
    if (not root.left) and (not root.right):
        return 0

    return 1 + max(height(root.left), height(root.right))
