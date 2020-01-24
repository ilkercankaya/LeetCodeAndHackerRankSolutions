# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def helper(start, end):
            if start == end:
                return TreeNode(nums[start])
            elif start > end:
                return None

            middle = ((end - start) // 2) + start
            root = TreeNode(nums[middle])
            root.left = helper(start, middle - 1)
            root.right = helper(middle + 1, end)

            return root

        return helper(0, len(nums) - 1)
