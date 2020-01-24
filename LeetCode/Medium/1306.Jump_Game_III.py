import queue


class Solution:
    def canReach(self, arr, start):
        if arr[start] == 0:
            return True

        visited = set([start])

        que = queue.Queue()

        que.put(start)

        while que.qsize() > 0:
            for i in range(que.qsize()):
                curIndex = que.get()

                for dir in [+arr[curIndex], -arr[curIndex]]:
                    neigIndex = curIndex + dir
                    neigVal = arr[neigIndex] if 0 <= neigIndex < len(arr) else -1

                    if neigVal == 0:
                        return True

                    if neigVal != -1 and neigIndex not in visited:
                        visited.add(neigIndex)
                        que.put(neigIndex)

        return False


s = Solution()
print(s.canReach([3,0,2,1,2],2))
