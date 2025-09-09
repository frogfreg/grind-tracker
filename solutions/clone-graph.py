"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
def cloneGraph(node):
    cloned = {}

    return cloneNode(node, cloned)


def cloneNode(node, cloned):
    if not node:
        return None

    if node.val in cloned:
        return cloned[node.val]

    res = Node(node.val, None)
    cloned[node.val] = res

    for nei in node.neighbors:
        newNei = cloneNode(nei, cloned)

        if newNei:
            res.neighbors.append(newNei)

    return res
