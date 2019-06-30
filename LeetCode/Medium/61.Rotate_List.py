# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(N) Time Complexity, O(1) Space Complexity, Two Pointers are used

class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return head

        length = 1
        copyHead = head

        while copyHead.next:
            copyHead = copyHead.next
            length += 1

        numOfNode = length - k % length - 1

        tail = head

        for i in range(numOfNode):
            tail = tail.next

        copyHead.next = head
        modifHead = tail.next
        tail.next = None

        return modifHead