import bisect


class Solution:
    def removeCoveredIntervals(self, intervals) -> int:

        total = rightWall = 0

        for start, end in sorted(intervals, key=lambda a: [a[0], -a[1]]):
            total += end <= rightWall
            rightWall = max(rightWall, end)

        return total