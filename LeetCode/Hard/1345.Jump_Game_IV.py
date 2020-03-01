import collections

class Solution:
    def minJumps(self, arr) -> int:
        teleporter = collections.defaultdict(list)

        for i, num in enumerate(arr):
            teleporter[num].append(i)


        q = collections.deque()

        q.append((0,0))

        visitedValues = set()
        visitedIndexes = set()

        visitedIndexes.add(0)

        dir = [-1 , +1]

        while len(q) > 0:
            currentIndex, cost = q.popleft()
            value = arr[currentIndex]

            if currentIndex == len(arr) - 1:
                return cost

            for inc in dir:
                newIndex = currentIndex + inc
                if 0 <= newIndex < len(arr) and newIndex not in visitedIndexes:
                    q.append((newIndex, cost + 1))
                    visitedIndexes.add(newIndex)

            if value not in visitedValues:
                for neig in teleporter[value]:
                    if neig not in visitedIndexes:
                        q.append((neig, cost + 1))

                visitedValues.add(value)

s = Solution()
print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
print(s.minJumps([7,6,9,6,9,6,9,7]))
print(s.minJumps([1]))
print(s.minJumps([11,22,7,7,7,7,7,7,7,22,13]))