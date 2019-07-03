"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque

        if not root:
            return root

        queue = deque()

        queue.append(root)

        while queue:

            queueHelper = deque()

            while queue:

                node = queue.popleft()

                if not queue:
                    node.next = None

                else:
                    node.next = queue[0]

                if node.left:
                    queueHelper.append(node.left)

                if node.right:
                    queueHelper.append(node.right)

            queue = queueHelper

        return root