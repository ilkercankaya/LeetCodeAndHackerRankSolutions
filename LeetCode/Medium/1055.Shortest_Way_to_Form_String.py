import collections
import bisect

class Solution:
    def shortestWay(self, source: str, target: str) -> int:


        def indexer():
            map = collections.defaultdict(list)
            for i, char in enumerate(source):
                map[char].append(i)

            return map

        indexMap = indexer()

        splitNum = 1

        delimiter = -2
        for i in range(len(target)):
            char = target[i]
            if char not in indexMap:
                return -1

            candidate = bisect.bisect_left(indexMap[char], delimiter + 1)

            if len(indexMap[char]) == candidate:
                candidate -= 1

            if indexMap[char][candidate] > delimiter:
                delimiter = indexMap[char][candidate]
            else:
                splitNum += 1
                delimiter = indexMap[char][0]


        return splitNum

