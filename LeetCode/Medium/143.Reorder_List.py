# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head) -> None:

        if not head or not head.next:
            return head

        slowPtr = fastPtr = head

        # find the middle
        while fastPtr.next and fastPtr.next.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # reverse from middle
        middle = slowPtr.next
        slowPtr.next = None
        prev = None

        while middle:
            nextMiddle = middle.next
            middle.next = prev
            prev = middle
            middle = nextMiddle

        firstList = head
        reversedList = prev


        # Merge Two Lists
        while firstList and reversedList:
            reversedListNext = reversedList.next
            firstsNext = firstList.next

            firstList.next = reversedList
            reversedList.next = firstsNext

            reversedList = reversedListNext
            firstList = firstsNext



