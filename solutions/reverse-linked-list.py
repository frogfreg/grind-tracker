# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(node):
    if not node:
        return None

    nodes = []
    curr = node
    while curr:
        nodes.append(curr.val)
        curr = curr.next

    nodes = nodes[::-1]

    head = None
    curr = None

    for n in nodes:
        newNode = ListNode(n)

        if not head:
            head = newNode
            curr = head
        else:
            curr.next = newNode
            curr = curr.next

    return head
