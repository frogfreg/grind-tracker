# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isValidBST(root):
    return validate(root, float("-inf"), float("inf"))


def validate(root, lowerLimit, upperLimit):
    if root.left:
        if (
            (root.left.val >= root.val)
            or (root.left.val <= lowerLimit)
            or not (validate(root.left, lowerLimit, min(upperLimit, root.val)))
        ):
            return False

    if root.right:
        if (
            (root.right.val <= root.val)
            or (root.right.val >= upperLimit)
            or (not validate(root.right, max(lowerLimit, root.val), upperLimit))
        ):
            return False

    return True
