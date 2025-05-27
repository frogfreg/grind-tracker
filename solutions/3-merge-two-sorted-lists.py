# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    p1 = list1
    p2 = list2

    finalHead = None
    curr = None

    while p1 or p2:
        newNode = None
        if p1 and p2:
            if p1.val < p2.val:
                newNode = ListNode(p1.val)
                p1 = p1.next
            else:
                newNode = ListNode(p2.val)
                p2 = p2.next

        elif p1:
            newNode = ListNode(p1.val)
            p1 = p1.next

        elif p2:
            newNode = ListNode(p2.val)
            p2 = p2.next

        if finalHead:
            curr.next = newNode
            curr = curr.next
        else:
            finalHead = newNode
            curr = finalHead

    return finalHead
