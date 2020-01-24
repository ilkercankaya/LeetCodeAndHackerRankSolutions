from collections import deque
class Solution:
    def widthOfBinaryTree(self, root) -> int:

        if not root:
            return 0

        maxWidth = 1

        pq = deque()
        pq.append((root,0))

        while len(pq) > 0:

            left, right = float("inf"), float("-inf")

            for _ in range(len(pq)):
                node, level = pq.popleft()
                left = min(left, level)
                right = max(right, level)

                if node.left:
                    pq.append((node.left, 2 * level))
                if node.right:
                    pq.append((node.right, 2 * level + 1))

            if left != right:
                maxWidth = max(maxWidth, right - left + 1)

        return maxWidth