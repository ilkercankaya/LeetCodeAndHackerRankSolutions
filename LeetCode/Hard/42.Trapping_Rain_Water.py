class Solution:
    def trap(self, height):
        leftMax = [0] * len(height)

        for i in range(1, len(height)):
            leftMax[i] = max(height[i - 1], leftMax[i - 1])

        rightMax = [0] * len(height)

        for i in range(len(height)-1)[::-1]:
            rightMax[i] = max(height[i + 1], rightMax[i + 1])

        return sum(max(0, min(leftMax[i], rightMax[i]) - height[i]) for i in range(1, len(height) - 1))
