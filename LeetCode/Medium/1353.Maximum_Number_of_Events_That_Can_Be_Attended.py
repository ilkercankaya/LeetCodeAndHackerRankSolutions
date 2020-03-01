import collections, heapq


class Solution:
    def maxEvents(self, events) -> int:
        if len(events) == 0:
            return 0

        startToEnd = collections.defaultdict(list)

        for start, end in events:
            startToEnd[start].append(end)

        res = 0
        q = []
        for i in range(min(events, key=lambda x: x[0])[0], max(events, key=lambda x: x[1])[1] + 1):
            for num in startToEnd[i]:
                heapq.heappush(q, num)

            while len(q) != 0 and q[0] < i:
                heapq.heappop(q)

            if len(q) != 0 and q[0] >= i:
                heapq.heappop(q)
                res += 1

        return res

s = Solution()
print(s.maxEvents([[1,2],[1,2],[1,6],[1,2],[1,2]]))