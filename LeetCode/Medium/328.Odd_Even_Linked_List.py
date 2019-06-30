# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(N), Space: O(1)
# Have two pointers jump twice while connecting each other and then connect them at last
# Modifies input

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(N), Space: O(1)
# Have two pointers jump twice while connecting each other and then connect them at last
# Modifies input

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        evenListHead = head.next
        odd = head
        even = head.next

        oddPrev = None
        evenPrev = None

        # pointers terminate at the same time - check only one
        while even and even.next:
            # first travel since modification will be done
            oddPrev = odd
            evenPrev = even

            even = even.next.next
            odd = odd.next.next

            oddPrev.next = odd
            evenPrev.next = even

        odd.next = evenListHead

        return head

