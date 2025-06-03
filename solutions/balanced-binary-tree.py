# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    if not root:
        return True

    if abs(height(root.left) - height(root.right)) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)


def height(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    return 1 + max(height(root.left), height(root.right))
