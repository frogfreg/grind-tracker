from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(root):
        if not root:
            return []

        q = deque()
        q.append((root, 0))

        valueList = []

        while q:
            tup = q.popleft()
            node, level = tup[0], tup[1]
            valueList.append((node.val, level))

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        currList = []
        currLevel = 0
        finalList = []

        for n in valueList:
            val, lev = n[0], n[1]

            if currLevel != lev:
                currLevel = lev
                finalList.append(currList)
                currList = []

            currList.append(val)

        finalList.append(currList)

        return finalList
