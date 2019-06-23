# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None

        sp, fp = head, head

        while fp and fp.next:

            fp = fp.next.next
            sp = sp.next
            if fp == sp:
                break

        if not fp:
            return None

        sp = head
        while sp != fp:
            sp = sp.next
            fp = fp.next

        return sp