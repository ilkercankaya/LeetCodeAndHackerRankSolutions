import queue

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        adjList = [[] * n for i in range(n)]
        for fromLoc, toLoc, price in flights:
            adjList[fromLoc].append((toLoc, price))

        priorityQueue = queue.PriorityQueue()
        # first field is cost second is counter third is location
        priorityQueue.put((0, -1, src))

        while priorityQueue.qsize() > 0:
            cheapestcurr = priorityQueue.get()
            if cheapestcurr[2] == dst:
                return cheapestcurr[0]


            for adj, cost in adjList[cheapestcurr[2]]:
                if cheapestcurr[1] + 1 <= K:
                    priorityQueue.put((cheapestcurr[0] + cost, cheapestcurr[1] + 1, adj))

        return -1




s = Solution()
print(s.findCheapestPrice(
5,
[[0,1,10],[1,2,10],[2,3,10],[3,4,10],[0,2,100]],
0,
4,
2
))
