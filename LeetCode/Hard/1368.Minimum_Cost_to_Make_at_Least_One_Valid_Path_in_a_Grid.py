import collections


class Solution:
    # 0 - 1 O(MN)
    def minCost(self, grid) -> int:
        pq = collections.deque()
        visited = set()
        pq.append((0, (0, 0)))

        dirs = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
        while len(pq) > 0:
            cost, node = pq.popleft()

            if node == (len(grid) - 1, len(grid[0]) - 1):
                return cost

            if node in visited:
                continue

            visited.add(node)

            for dir in dirs:
                newX, newY = dir[0] + node[0], dir[1] + node[1]

                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
                    # cost is 0
                    if dir == dirs[grid[node[0]][node[1]] - 1]:
                        pq.appendleft((cost, (newX, newY)))
                        # cost is 1
                    else:
                        pq.append((cost + 1, (newX, newY)))

        return -1

    # Djisktra O(MNlog(MN))
    # def minCost(self, grid) -> int:
    #     pq = queue.PriorityQueue()
    #     visited = set()
    #     pq.put((0, (0, 0)))
    #
    #     dirs = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
    #     while pq.qsize() > 0:
    #         cost, node = pq.get()
    #
    #         if node == (len(grid) - 1, len(grid[0]) - 1):
    #             return cost
    #
    #         if node in visited:
    #             continue
    #
    #         visited.add(node)
    #
    #         for dir in dirs:
    #             newX, newY = dir[0] + node[0], dir[1] + node[1]
    #
    #             inc = 0 if dir == dirs[grid[node[0]][node[1]] - 1] else 1
    #             if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
    #                 pq.put((cost + inc, (newX, newY)))
    #
    #     return -1