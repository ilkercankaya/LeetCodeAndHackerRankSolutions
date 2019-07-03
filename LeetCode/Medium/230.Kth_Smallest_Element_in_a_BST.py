class Solution:
    def kthSmallest(self, root, k: int) -> int:

        if not root:
            return root

        stack = []

        node = root
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            node = node.right
