class Solution:
    def maxSumBST(self, root) -> int:
        maxSum = 0

        def postOrderDFS(root):
            # the idea is if a subtree S is a BST then if another tree T containing root Tn and S as a left or right children is also a BST under two conditions:
            # 1. if S is left child of Tn then max(S) < Tn.val
            # 2. if S is the right child then min(S) > Tn.val
            # do these checks in an inductive manner to find the largest BSt while keeping track of the subtrees sum
            if not root:
                return [float("inf"), float("-inf"), 0]

            leftMin, leftMax, leftSum = postOrderDFS(root.left)
            rightMin, rightMax, rightsum = postOrderDFS(root.right)

            nonlocal maxSum

            # validate BST
            if leftMax < root.val < rightMin:
                maxSum = max(maxSum, leftSum + rightsum + root.val)
                return [min(leftMin, rightMin, root.val), max(leftMax, rightMax, root.val),
                        leftSum + rightsum + root.val]
            else:
                # if the current tree isnt a BST then any bigger tree containing this nonBST subtree is a invalid BST
                return [float("-inf"), float("+inf"), 0]

        postOrderDFS(root)
        return maxSum
