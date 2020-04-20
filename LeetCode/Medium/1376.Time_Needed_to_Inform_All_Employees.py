import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        totalTime = 0

        adjList = collections.defaultdict(list)

        for i, num in enumerate(manager):
            if num != -1:
                adjList[num].append(i)

        q = collections.deque()
        q.append((headID, 0))

        while len(q) > 0:
            top, cost = q.popleft()

            totalTime = max(totalTime, cost)
            for neig in adjList[top]:
                q.append((neig, cost + informTime[top]))


        return totalTime