# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head

        fastPtr = head

        for i in range(n):
            fastPtr = fastPtr.next

        if fastPtr is None:
            return head.next

        slowPtr = head

        while fastPtr.next is not None:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next

        slowPtr.next = slowPtr.next.next

        return head

