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

    # I have made this proof. I believe that Time complexity is in fact O(N * H).
    # Imagine a perfect BT: Height is H and LL length is H + 1 (To have a mismatch so that algo doesn't terminate early).
    # Imagine each node have 1s and LL contains 1s only too.
    # So
    # Tree is like:
    #  1
    # | |
    # 1  1
    # .......
    # In each row you do the following operations:
    # For the first row yo do 2^H work due to the DFS check,
    # in the second row you do 2^(H - 1) of work for 2 nodes so it is 2 * 2^(H - 1)
    # For the third row you do 2^(H-3) of work for 4 nodes so it is 4 * 2^(H - 2)
    # The Time complexity is:
    # Sigma 2^(i) * 2^(H - i)
    # for i in 0 to H.
    #
    # We can see that 2^(-i) will cancel 2^i out so it will just be 2^H. Since we do this H times, the end time complexity is H * 2^H.
    # Notice H = logN, therefore, 2^H = N. This will give us N* H for the worst case.
    # O(NH)
    def isSubPath(self, head, root) -> bool:
        if not head:
            return True

        if not root:
            return False

        def dfs(head, root):
            if not head: return True
            if not root: return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))

        return dfs(head,root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    # If we assume head in path uses a pattern algorithm like KMP then this is indeed O(N* H) Time Complexity
    # O(N * L)
    # def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
    #         res = []
    #         while head:
    #             res.append(str(head.val))
    #             head = head.next
    #         head = "".join(res)
    #
    #         def dfs(root, path):
    #             if head in path:
    #                 return True
    #             if not root:
    #                 return False
    #             return dfs(root.left, path + str(root.val)) or dfs(root.right, path + str(root.val))
    #
    #         return dfs(root, "")