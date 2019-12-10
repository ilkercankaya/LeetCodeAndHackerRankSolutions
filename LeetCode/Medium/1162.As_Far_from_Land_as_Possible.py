from collections import deque


class Solution:
    def maxDistance(self, grid) -> int:

        queue = deque()

        m, n = len(grid), len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    queue.append((i, j))

        directions = [(0, +1), (0, -1), (+1, 0), (-1, 0)]

        if len(queue) == m * n or len(queue) == 0:
            return -1

        level = -1
        while queue:

            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()

                for incX, incY in directions:
                    newX = x + incX
                    newY = y + incY

                    if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == 0:
                        grid[newX][newY] = 1
                        queue.append((newX, newY))

            level += 1

        return level

