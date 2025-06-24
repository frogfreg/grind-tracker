# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middleNode(head):
    curr = head
    count = 0

    while curr:
        count += 1
        curr = curr.next

    middle = count // 2

    curr = head
    count = 0
    while count < middle:
        curr = curr.next
        count += 1

    return curr
