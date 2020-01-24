import queue


class Solution:
    def wallsAndGates(self, rooms) -> None:

        if not rooms:
            return

        queueBFS = queue.Queue()

        # find the roots for the bfs
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    queueBFS.put((i, j))

        directions = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
        # do bfs and update on the fly
        while not queueBFS.empty():
            currX, currY = queueBFS.get()

            for xInc, yInc in directions:
                newX, newY = currX + xInc, currY + yInc

                if 0 <= newX < len(rooms) and 0 <= newY < len(rooms[0]) and rooms[newY][newY] == 2147483647:
                    rooms[newX][newY] = rooms[currX][currY] + 1
                    queueBFS.put((newX, newY))

s = Solution()
print(s.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))