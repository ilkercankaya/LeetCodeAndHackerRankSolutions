from collections import defaultdict
import queue


class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        adjList = defaultdict(dict)

        for fro, to, cost in edges:
            adjList[fro][to] = cost
            adjList[to][fro] = cost

        results = []

        def bfs(id):
            visited = set()
            q = queue.PriorityQueue()

            q.put((0, id))

            res = set()
            while q.qsize() > 0:
                curCost, curID = q.get()

                if curID in visited:
                    continue
                for to, newCost in adjList[curID].items():
                    finalCost = curCost + newCost
                    if to not in visited and finalCost <= distanceThreshold:
                        res.add(to)
                        q.put((finalCost, to))
                visited.add(curID)

            results.append((len(res), id))

        for i in range(n):
            bfs(i)

        return sorted((results), key=lambda x: (x[0], -x[1]))[0][1]

s = Solution()
# print(s.findTheCity(4
# ,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# ,4))
# print(s.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2))
# print(s.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2))
print(s.findTheCity(8
,[[3,5,9558],[1,2,1079],[1,3,8040],[0,1,9258],[4,7,7558],[5,6,8196],[3,4,7284],[1,5,6327],[0,4,5966],[3,6,8575],[2,5,8604],[1,7,7782],[4,6,2857],[3,7,2336],[0,6,6],[5,7,2870],[4,5,5055],[0,7,2904],[1,6,2458],[0,5,3399],[6,7,2202],[0,2,3996],[0,3,7495],[1,4,2262],[2,6,1390]]
,7937))
