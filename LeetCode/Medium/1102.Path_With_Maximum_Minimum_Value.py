# Biweekly Contest 3

import queue


class Solution:
    def maximumMinimumPath(self, A):
        if len(A) == 0:
            return 0

        target = (len(A) - 1, len(A[0]) - 1)

        pq = queue.PriorityQueue()
        visited = set()
        visited.add((0, 0))
        pq.put((-A[0][0], (0, 0)))

        directions = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
        while pq.qsize() > 0:
            curNode = pq.get()
            x, y = curNode[1]
            if curNode[1] == target:
                return -curNode[0]

            for incX, incY in directions:
                newX = x + incX
                newY = y + incY

                if 0 <= newX < len(A) and 0 <= newY < len(A[0]) and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    pq.put((max(curNode[0], -A[newX][newY]), (newX, newY)))


s = Solution()
print(s.maximumMinimumPath([[5, 4, 5], [1, 2, 6], [7, 4, 6]]))
