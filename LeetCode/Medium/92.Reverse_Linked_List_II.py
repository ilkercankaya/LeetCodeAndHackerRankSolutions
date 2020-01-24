# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m: int, n: int):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        parent = dummyNode

        # iter m to its position
        for i in range(m - 1):
            parent = parent.next

        reverse = None
        cur = parent.next

        for i in range(n - m + 1):
            curNext = cur.next
            cur.next = reverse
            reverse = cur
            cur = curNext


        parent.next.next = cur
        parent.next = reverse

        return dummyNode.next
