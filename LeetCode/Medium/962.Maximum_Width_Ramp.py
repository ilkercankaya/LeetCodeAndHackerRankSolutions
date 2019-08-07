class Solution:
    def maxWidthRamp(self, A) -> int:
        maxRes = 0
        localMin = float("inf")

        for num in sorted(range(len(A)), key=A.__getitem__):
            maxRes = max(maxRes, num - localMin)
            localMin = min(localMin, num)

        return maxRes