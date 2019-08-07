import collections, queue


class Solution:
    def networkDelayTime(self, times, N, K):
        K -= 1
        shortestCosts = [float("inf")] * N
        shortestCosts[K] = 0
        adjList = collections.defaultdict(list)

        for parent, child, cost in times:
            parent -= 1
            child -= 1
            adjList[parent].append((child, cost))

        priorityQueue = queue.PriorityQueue()
        priorityQueue.put((0, K))
        visited = set()
        while priorityQueue.qsize() > 0:
            costPar, parent = priorityQueue.get()

            if parent not in visited:
                for adj in adjList[parent]:
                    child, cost = adj
                    if costPar + cost < shortestCosts[child]:
                        shortestCosts[child] = costPar + cost
                        priorityQueue.put((shortestCosts[child], child))
            visited.add(parent)

        if float("inf") in shortestCosts:
            return -1

        return max(shortestCosts)
