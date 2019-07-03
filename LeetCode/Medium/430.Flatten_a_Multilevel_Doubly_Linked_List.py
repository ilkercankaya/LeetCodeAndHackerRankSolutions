"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# beats 82.34%
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def flatten(self, head: 'Node', furtherNode=None) -> 'Node':

        if not head:
            return

        cloneHead = head

        prev = None

        while cloneHead:
            if cloneHead.child:
                nextNode = cloneHead.next
                subListHead = self.flatten(cloneHead.child, nextNode)
                cloneHead.child = None
                cloneHead.next = subListHead
                subListHead.prev = cloneHead
                cloneHead = nextNode
            else:
                prev = cloneHead
                cloneHead = cloneHead.next

        if prev:
            prev.next = furtherNode

        if furtherNode:
            furtherNode.prev = prev

        return head