class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals

        intervals.sort()
        result = []

        for start, end in intervals:
            if len(result) == 0 or result[-1][1] < start:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result
