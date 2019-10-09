class Solution:
    def maxArea(self, height) -> int:
        l = 0
        r = len(height) - 1

        maxArea = 0

        while l < r:
            maxArea = max(maxArea, min(height[r], height[l]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
