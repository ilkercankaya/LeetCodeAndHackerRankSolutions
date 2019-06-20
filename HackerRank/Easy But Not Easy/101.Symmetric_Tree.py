# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 40 ms, faster than 81.64%

class Solution:
    def _sym(self, left, right):
        if not left and not right:
            return True

        if (left and not right) or (not left and right):
            return False

        if left.val == right.val:
            return self._sym(left.left, right.right) and self._sym(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        return self._sym(root.left, root.right) and self._sym(root.right, root.left)



# 40 ms, faster than 81.64%

from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        stack = deque([(root.left, root.right)])

        while stack:
            left, right = stack.pop()

            if left is None and right is None:
                continue

            if (left is None) ^ (right is None):
                return False
            elif left.val != right.val:
                return False

            stack.extend([(left.left, right.right), (left.right, right.left)])

        return True