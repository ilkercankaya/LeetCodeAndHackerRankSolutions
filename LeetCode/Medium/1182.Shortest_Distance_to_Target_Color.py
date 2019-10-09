import collections
import bisect

class Solution:
    def shortestDistanceColor(self, colors, queries):
        colorDic = collections.defaultdict(list)

        for i, color in enumerate(colors):
            colorDic[color].append(i)

        results = []

        for i, color in queries:
            if color not in colorDic:
                results.append(-1)
                continue

            index = bisect.bisect_left(colorDic[color], i)

            if index >= len(colorDic[color]):
                results.append(i - colorDic[color][-1])
            else:
                results.append(min(abs(i - colorDic[color][index]), abs(i - colorDic[color][index - 1])))

        return results