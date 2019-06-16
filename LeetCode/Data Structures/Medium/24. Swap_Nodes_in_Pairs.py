# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # no other two nodes exist
        if not (head and head.next):
            return head

        # get the nodes
        current = head
        nextNode = head.next

        # swap nodes - nextNode is in first position and current is at second - they are swapped
        current.next = self.swapPairs(nextNode.next)
        nextNode.next = current

        # since we swapped the nodes we need to
        return nextNode

