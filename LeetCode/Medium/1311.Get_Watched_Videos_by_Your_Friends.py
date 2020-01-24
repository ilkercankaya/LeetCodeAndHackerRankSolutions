import queue
from collections import Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id: int, level: int):

        depth = 0
        q = queue.Queue()
        visited = set()

        q.put(id)
        visited.add(id)

        while q.qsize() > 0 and depth != level:
            for i in range(q.qsize()):
                node = q.get()
                for friend in friends[node]:
                    if friend not in visited:
                        q.put(friend)
                        visited.add(friend)

            depth += 1

        if q.qsize() == 0:
            return []

        watchedDepth = [watched for _ in range(q.qsize()) for watched in watchedVideos[q.get()]]

        watchedDepth = [(val, key) for key, val in Counter(watchedDepth).items()]
        watchedDepth.sort()

        return list(map(lambda x: x[1], watchedDepth))


s = Solution()
print(s.watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]]
,[[1,2],[0,3],[0,3],[1,2]]
,0
,1))