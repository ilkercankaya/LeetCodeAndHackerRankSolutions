# Solution One
class Solution(object):
    def isValidBST(self, root, min=None, max=None):

        if not root:
            return True

        if (min and root.val <= min.val) or (max and root.val >= max.val):
            return False

        return self.isValidBST(root.left, min, root) and self.isValidBST(root.right, root, max)

# Solution Two
# class Solution(object):
#     def __init__(self):
#         self.prev = None
#
#     def isValidBST(self, root):
#         if not root:
#             return True
#
#         if not self.isValidBST(root.left):
#             return False
#
#         if self.prev and self.prev.val >= root.val:
#             return False
#
#         self.prev = root
#
#         return self.isValidBST(root.right)
