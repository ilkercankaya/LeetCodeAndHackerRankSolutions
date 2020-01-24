import queue


class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1

        q = queue.Queue()
        q.put((0, 0))

        visited = set()
        level = 0

        dir = [(0, +1), (0, -1), (+1, 0), (-1, 0), (-1, -1), (-1, +1), (+1, -1), (+1, +1)]

        while q.qsize() > 0:
            level += 1

            for i in range(q.qsize()):
                row, col = q.get()

                if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                    return level

                for xInc, yInc in dir:
                    newX = xInc + row
                    newY = yInc + col

                    if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and (newX, newY) not in visited and \
                            grid[newX][newY] == 0:
                        visited.add((newX, newY))
                        q.put((newX, newY))

        return -1
